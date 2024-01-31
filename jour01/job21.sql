mysql> SELECT COUNT(*) AS nombre_etudiants FROM etudiant
    ->  where age between 18 and 25;
+------------------+
| nombre_etudiants |
+------------------+
|                3 |
+------------------+
1 row in set (0.00 sec)