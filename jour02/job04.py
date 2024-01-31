import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="laplateforme",
)

cursor = db.cursor()

cursor.execute("SELECT nom, capacite FROM salle")
result = cursor.fetchall()
print(result)

cursor.close()
db.close()