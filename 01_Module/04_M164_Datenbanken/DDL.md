
# DDL - Data Definition Language
Hier wird die Struktur erstellt, wo die Daten erfasst werden können. Vorerst müssen aber Tabellen mit Attributen erstellt werden. 
### CREATE Befehl
Mit dem Befehl `CREATE SCHEMA;` oder `CREATE DATABASE;` wird eine Datenbank erstellt. `CREATE TABLE;` erstellt eine Tabelle, in der man Attribute mit Datentypen hinzufügen kann. 

### DROP Befehl;
Mit dem Befehl `DROP TABLE` löscht man Tabellen. Es ist allerdings wichtig, dass man sich mehrmals überlegt, etwas zu löschen, weil es nicht wiederhergestellt werden kann. `DROP DATABASE;` löscht eine ganze Datenbank. 

### ALTER TABLE
Mit `ALTER TABLE beispiel_table` kann man Tabellen bearbeiten. 

Hier das Script: 
```
CREATE TABLE employees (
id INTEGER AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(50),
email VARCHAR(100),
hire_date DATE,
salary DECIMAL(10,2)
);

ALTER TABLE employees ADD department VARCHAR(50);

ALTER TABLE employees MODIFY salary Float(10.2);

ALTER TABLE employees RENAME COLUMN department TO department_id;

ALTER TABLE employees MODIFY department INT;

ALTER TABLE employees DROP COLUMN email;
```