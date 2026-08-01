import mysql.connector
import time

connection = None

while connection is None:
    try:
        connection = mysql.connector.connect(
            host="mysql",
            user="root",
            password="2027",
            database="devops_db"
        )
        print(" Connected to MySQL")

    except mysql.connector.Error:
        print(" MySQL not ready. Retrying in 5 seconds...")
        time.sleep(5)