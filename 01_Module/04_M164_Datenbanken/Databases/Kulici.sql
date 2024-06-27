# 1
CREATE SCHEMA db_ubs;
USE db_ubs;
# 2
CREATE TABLE db_ubs.kundeninfo (
ID_Kunde INT auto_increment NOT NULL PRIMARY KEY,
Nachname VARCHAR(50) NOT NULL,
Kontonummer VARCHAR(5) NOT NULL,
SWIFT INT,
Kontostand DECIMAL(10.2),
Erstellt_am DATE
);
# 3
INSERT INTO kundeninfo VALUES (
NULL, "Kulici", 15512, 1234567891, 250000.70, 140324
);
# 4
INSERT INTO kundeninfo(Nachname, Kontonummer, SWIFT, Kontostand) VALUES (
"Kellenberger", 81841, 7610284172, 50
);

# 5
ALTER TABLE kundeninfo ADD geändert_am DateTime;
# 6
UPDATE kundeninfo SET Kontostand = Kontostand + 1000 WHERE Nachname = "Kulici";
# 7
SELECT ID_Kunde, Nachname, Kontonummer, Kontostand FROM kundeninfo WHERE Nachname LIKE "Kel@"  OR Kontonummer > 3322 AND Kontostand >= 100 ORDER BY Nachname, Kontostand DESC ; 