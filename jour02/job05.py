import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="laplateforme",
)

cursor = db.cursor()

cursor.execute("SELECT SUM(superficie) as superficie FROM etage")
result = cursor.fetchone()[0]
print(f'La superficie de la Plateforme est de {result} m²')

cursor.close()
db.close()