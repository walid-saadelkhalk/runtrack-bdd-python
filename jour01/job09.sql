mysql> select * from etudiant
    -> order by age asc;
+----+--------+-----------+-----+---------------------------------+
| id | nom    | prenom    | age | email                           |
+----+--------+-----------+-----+---------------------------------+
|  4 | Binkie | Barnes    |  16 | binkie.barnes@laplateforme.io   |
|  3 | Doe    | John      |  18 | john.doe@laplateforme.io        |
|  5 | Dupuis | Gertrude  |  20 | gertrude.dupuis@laplateforme.io |
|  1 | Betty  | Spaghetti |  23 | betty.spaghetti@laplateforme.io |
|  2 | Chuck  | Steak     |  45 | chuck.steak@laplateforme.io     |
+----+--------+-----------+-----+---------------------------------+
5 rows in set (0.00 sec)