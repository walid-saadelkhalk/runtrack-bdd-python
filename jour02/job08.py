import mysql.connector

class Directeur:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def create_animal(self, nom, race, id_cage, naissance, origine):
        query = "Insert INTO animal (nom, race, id_cage, naissance, origine) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, race, id_cage, naissance, origine)
        self.cursor.execute(query, values)
        self.db.commit()
        return f"Animal {nom} ajouté avec succès."

    def create_cage(self, quantite, superficie, capacite_max):
        query = "Insert INTO cage (quantite, superficie, capacite_max) VALUES (%s, %s, %s)"
        values = (quantite, superficie, capacite_max)
        self.cursor.execute(query, values)
        self.db.commit()
        return f"Cette cage peut contenir {capacite_max} animaux."

    def delete_animal(self, id):
        query = "DELETE FROM animal WHERE id = %s"
        values = (id,)
        self.cursor.execute(query, values)
        self.db.commit()
        return f"Animal {id} supprimé avec succès."

    def delete_cage(self, id):
        query = "DELETE FROM cage WHERE id = %s"
        values = (id,)
        self.cursor.execute(query, values)
        self.db.commit()
        return f"Cage {id} supprimée avec succès."

    def update_animal(self, id_cage,nom):
        query = "UPDATE animal SET id_cage = %s WHERE nom = %s"
        values = (id_cage, nom)
        self.cursor.execute(query, values)
        self.db.commit()
        return f"Animal {nom} est dans la cage {id_cage}."
    
    def update_cage(self, id, quantite):
        query = "UPDATE cage SET quantite = %s WHERE id = %s"
        values = (quantite, id)
        self.cursor.execute(query, values)
        self.db.commit()
        return f"La cage {id} contient {quantite} animaux."

    def total_animaux(self):
        query = "SELECT SUM(quantite) FROM cage"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def liste_en_cage(self):
        query = "SELECT animal.nom, cage.quantite FROM animal JOIN cage ON animal.id_cage = cage.id"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def superficie_totale(self):
        query = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def read_animal(self):
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        return self.cursor.fetchall()



directeur = Directeur(host="localhost", user="root", password="", database="zoo")

# Créer un animal
# print(directeur.create_animal(nom="Pluto", race="Singe", id_cage=2, naissance="2023-01-01", origine="Kenya"))
# print(directeur.create_animal(nom="Mickey", race="Elephant", id_cage=1, naissance="2019-01-01", origine="Kenya"))
# print(directeur.create_animal(nom="Luce", race="Lion", id_cage=3, naissance="2020-01-01", origine="Maroc"))
# print(directeur.create_animal(nom="Juste", race="Lion", id_cage=3, naissance="2018-01-01", origine="Maroc"))
# print(directeur.create_animal(nom="George", race="Gorille", id_cage=3, naissance="2017-01-01", origine="Kenya"))

# Créer une cage
# print(directeur.create_cage(quantite=1, superficie=50, capacite_max=10))
# print(directeur.create_cage(quantite=1, superficie=100, capacite_max=20))
# print(directeur.create_cage(quantite=3, superficie=150, capacite_max=30))

# Mettre à jour la cage d'un animal
# print(directeur.update_animal(id_cage=23, nom="George"))


print(directeur.read_animal())


# Obtenir la liste des animaux et le nombre d'animaux dans chaque cage
print("Liste des animaux dans chaque cage:", directeur.liste_en_cage())

# Obtenir la superficie totale de toutes les cages
print("Superficie totale de toutes les cages:", directeur.superficie_totale())


# print(directeur.delete_cage(20))
# print(directeur.delete_animal(12))

directeur.cursor.close()
directeur.db.close()

    