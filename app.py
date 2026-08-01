from flask import Flask, render_template, request, redirect, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from db import connection

app = Flask(__name__)
app.secret_key = "devops_project_secret_key"


# ==========================
# Home
# ==========================
@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# Register
# ==========================
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        cursor = connection.cursor()

        sql = """
        INSERT INTO users (username, email, password)
        VALUES (%s, %s, %s)
        """

        cursor.execute(sql, (username, email, hashed_password))

        connection.commit()
        cursor.close()

        flash("Registration Successful! Please Login.", "success")

        return redirect("/login")

    return render_template("register.html")


# ==========================
# Login
# ==========================
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM users WHERE email=%s",
            (email,)
        )

        user = cursor.fetchone()

        cursor.close()

        if user:

            if check_password_hash(user["password"], password):

                session["username"] = user["username"]
                session["user_id"] = user["id"]

                flash("Login Successful!", "success")

                return redirect("/dashboard")

        flash("Invalid Email or Password!", "danger")

        return redirect("/login")

    return render_template("login.html")


# ==========================
# Dashboard
# ==========================
@app.route("/dashboard")
def dashboard():

    if "username" not in session:
        flash("Please login first.", "warning")
        return redirect("/login")

    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM notes WHERE user_id=%s",
        (session["user_id"],)
    )

    notes = cursor.fetchall()

    cursor.close()

    return render_template(
        "dashboard.html",
        username=session["username"],
        notes=notes
    )


# ==========================
# Add Note
# ==========================
@app.route("/add_note", methods=["POST"])
def add_note():

    if "username" not in session:
        flash("Please login first.", "warning")
        return redirect("/login")

    title = request.form["title"]
    content = request.form["content"]

    cursor = connection.cursor()

    sql = """
    INSERT INTO notes (user_id, title, content)
    VALUES (%s, %s, %s)
    """

    cursor.execute(
        sql,
        (session["user_id"], title, content)
    )

    connection.commit()

    cursor.close()

    flash("Note Added Successfully!", "success")

    return redirect("/dashboard")


# ==========================
# Delete Note
# ==========================
@app.route("/delete_note/<int:note_id>", methods=["POST"])
def delete_note(note_id):

    if "username" not in session:
        flash("Please login first.", "warning")
        return redirect("/login")

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM notes WHERE id=%s AND user_id=%s",
        (note_id, session["user_id"])
    )

    connection.commit()

    cursor.close()

    flash("Note Deleted Successfully!", "warning")

    return redirect("/dashboard")


# ==========================
# Logout
# ==========================
@app.route("/logout")
def logout():

    session.clear()

    flash("Logged Out Successfully!", "info")

    return redirect("/login")


# ==========================
# Run App
# ==========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)