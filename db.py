import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2027",
    database="devops_db"
)

print("Database Connected Successfully!")