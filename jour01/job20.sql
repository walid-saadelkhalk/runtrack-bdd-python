mysql> SELECT COUNT(*) AS nombre_etudiants FROM etudiant
    -> where age < 18;
+------------------+
| nombre_etudiants |
+------------------+
|                1 |
+------------------+
1 row in set (0.00 sec)