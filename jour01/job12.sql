mysql> insert into etudiant ( nom, prenom, age, email)
    -> values
    -> ('Dupuis', 'Martin', 18, 'martin.dupuis@laplateforme.io');
Query OK, 1 row affected (0.00 sec)

mysql> select * from etudiant
    -> where nom = 'Dupuis';
+----+--------+----------+-----+---------------------------------+
| id | nom    | prenom   | age | email                           |
+----+--------+----------+-----+---------------------------------+
|  5 | Dupuis | Gertrude |  20 | gertrude.dupuis@laplateforme.io |
|  6 | Dupuis | Martin   |  18 | martin.dupuis@laplateforme.io   |
+----+--------+----------+--