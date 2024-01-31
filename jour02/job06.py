import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="laplateforme",
)

cursor = db.cursor()

cursor.execute("SELECT SUM(capacite) as capacite FROM salle")
result = cursor.fetchone()[0]
print(f'La capacite de toutes les salles est de: {result}')

cursor.close()
db.close()