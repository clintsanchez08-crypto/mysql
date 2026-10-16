import sys

import mysql.connector

HOST = "localhost"
USER = "root"
PASSWORD = ""
DATABASE = "clintsanchez"
TABLE = "users"

try:
    db = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
    )
except mysql.connector.Error as err:
    print("ERROR: Not connected to MySQL.")
    print(f"Reason: {err}")
    print("Make sure MySQL is running in XAMPP and the settings above are correct.")
    sys.exit(1)

if db.is_connected():
    print("Connected to MySQL successfully.")
else:
    print("ERROR: Not connected to MySQL.")
    sys.exit(1)

cursor = db.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")
cursor.execute(f"USE {DATABASE}")

db.close()
