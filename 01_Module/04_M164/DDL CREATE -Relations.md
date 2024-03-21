# Fragen 
1. Erstellen Sie einen allgemeinen Syntax für die CONSTRAINT-Anweisung.
2. Wie wird beim Fremdschlüssel der Constraint NOT NULL erstellt?
3. Weshalb wird für jeden Fremdschlüssel ein Index erstellt? Lesen Sie [hier](https://www.datenbanken-verstehen.de/datenmodellierung/datenbank-index/)!
4. Wie wird der Constraint UNIQUE für ein Fremdschlüssel in Workbench mit Forward Engineering erstellt?

1.
```
 CONSTRAINT `fk_tbl_Fahrer_tbl_Bus`
    FOREIGN KEY (`tbl_Bus_ID_Bus`)
    REFERENCES `tbl_Bus` (`ID_Bus`) 
```
2.
```
CREATE INDEX `fk_tbl_Fahrer_tbl_Bus_idx` ON `tbl_Fahrer` (`tbl_Bus_ID_Bus` ASC) VISIBLE;
```
3.
