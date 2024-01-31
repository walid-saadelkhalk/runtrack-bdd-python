import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="entreprise",
)

cursor = db.cursor()

cursor.execute("SELECT nom, prenom, salaire FROM employe WHERE salaire > 3000")
result = cursor.fetchall()
print(result)

cursor.close()

second_cursor = db.cursor()

second_cursor.execute("SELECT employe.id, employe.nom, employe.prenom, employe.salaire, service.nom as service from employe join service on employe.id_service = service.id")

result2 = second_cursor.fetchall()
print(result2)

second_cursor.close()
db.close()





class Employe:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def create_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.db.commit()
        return f"Employe {prenom} {nom} ajouté avec succès."

    def read_employes_biens_payes(self, threshold):
        query = "SELECT nom, prenom, salaire FROM employe WHERE salaire > %s"
        values = (threshold,)
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def read_employes_et_services(self):
        query = "SELECT employe.id, employe.nom, employe.prenom, employe.salaire, service.nom as service FROM employe JOIN service ON employe.id_service = service.id"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_employe_service(self, employe_id, new_service_id):
        query = "UPDATE employe SET id_service = %s WHERE id = %s"
        values = (new_service_id, employe_id)
        self.cursor.execute(query, values)
        self.db.commit()
        return f"Service de l'employe avec ID {employe_id} mis à jour avec succès."

    def delete_employe(self, employe_id):
        query = "DELETE FROM employe WHERE id = %s"
        values = (employe_id,)
        self.cursor.execute(query, values)
        self.db.commit()
        return f"Employe avec ID {employe_id} supprimé avec succès."

    def __del__(self):
        self.cursor.close()
        self.db.close()

employe_manager = Employe("localhost", "root", "SYoccMwwade13+", "entreprise")

print(employe_manager.create_employe("Vanni", "Barbara", 1, 3))
print(employe_manager.create_employe("Mido", "Ban", 1000, 3))
print(employe_manager.read_employes_biens_payes(3000))
print(employe_manager.employes_et_services())
print(employe_manager.update_employe_service(1, 2))
print(employe_manager.delete_employe(6))

del employe_manager 
