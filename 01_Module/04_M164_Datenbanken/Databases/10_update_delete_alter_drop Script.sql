# 1. Beim Regisseur «Cohen» fehlt der Vorname. Vervollständigen sie den Regisseur Namen mit dem Vornamen «Etan».
# 2. Der Film «Angst» dauert nicht 92 Minuten, sondern 120 Minuten. Korrigieren Sie.
# 3. DVD gibt es nicht mehr. Das Sortiment wurde durch «Bluray» Medien ersetzt. Nennen Sie die Tabelle um nach «bluray_sammlung».
# 4. Eine neue Spalte «Preis» soll hinzugefügt werden.
# 5. Der Film «Angriff auf Rom» von Steven Burghofer wurde aus dem Sortiment entfernt. Bereinigen Sie die Tabelle.
# 6. Die Spalte «filme» soll nach «kinofilme» umbenannt werden.
# 7. Die Spalte Nummer wird nicht mehr benötigt. Löschen Sie sie.
# 8. Der Filmverleih rentiert nicht mehr. Die Firma wurde geschlossen und folglich werden alle Daten eliminiert. Löschen Sie die Tabelle.

select * from dvd_sammlung;
select * from bluray_sammlung;

# 1.
UPDATE dvd_sammlung SET regisseur =  "Etan Cohen" WHERE id = 4;
# 2
UPDATE dvd_sammlung SET laenge_minuten = 120 WHERE film = "Angst";
# 3
RENAME TABLE dvd_sammlung TO bluray_sammlung;
# 4 
ALTER TABLE bluray_sammlung ADD Preis INT unsigned;
# 5
DELETE FROM bluray_sammlung WHERE regisseur = "Steven Burghofer";
# 6
ALTER TABLE bluray_sammlung RENAME COLUMN film TO kinofilme;
# 7 
ALTER TABLE bluray_sammlung DROP COLUMN nummer;
# 8 
DROP TABLE bluray_sammlung;