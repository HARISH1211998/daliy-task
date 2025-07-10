import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdb"
)

cursor=con.cursor()
cursor.execute("SELECT * FROM your_table")
results = cursor.fetchall()
for row in results:
    print(row)

conn.close()