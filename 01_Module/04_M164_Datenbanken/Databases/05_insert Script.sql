CREATE TABLE kunden (kunde_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, vorname VARCHAR(255), nachname VARCHAR(255), land_id INT, wohnort VARCHAR(255));

#a.	Legen Sie mit der Kurzform einen Kunden mit folgenden Daten an: Heinrich Schmitt aus Zürich, Schweiz (Schweiz hat die land_id 2).
#b.	Legen Sie mit der Kurzform eine Kundin mit folgenden Daten an: Sabine Müller aus Bern, Schweiz (Schweiz hat die land_id 2).
#c.	Legen Sie mit der Kurzform einen Kunden mit folgenden Daten an: Markus Mustermann aus Wien, Österreich (Österreich hat die land_id 1).
#d.	Legen Sie mit der Langform einen Kunden mit folgenden Daten an: Herr Maier.
#e.	Legen Sie mit der Langform einen Kunden mit folgenden Daten an: Herr Bulgur aus Sirnach.
#f.	Legen Sie mit der Langform einen Kunden mit folgenden Daten an: Maria Manta.

select * from kunden;

# a
INSERT INTO kunden VALUES (NULL, "Heinrich", "Schmitt", 2, "Zürich");

# b
INSERT INTO kunden VALUES (NULL, "Sabine", "Müller", 2, "Bern");

# c
INSERT INTO kunden VALUES (NULL, "Markus", "Mustermann", 1, "Wien");

# d
INSERT INTO kunden (vorname, nachname) VALUES
("Herr", "Mayer");

# e
INSERT INTO kunden (vorname, nachname, wohnort) VALUES
("Herr", "Bulgur", "Sirnach");

# f
INSERT INTO kunden (vorname, nachname) VALUES
("Maria", "Manta");

# Richtig & Falsch korrigieren


#a.
INSERT INTO (nachname, wohnort, land_id) VALUES ('Fesenkampp', 'Duis-burg', 3);
# Lösung
INSERT INTO kunden (nachname, wohnort, land_id) VALUES ('Fesenkampp', 'Duis-burg', 3);
# Tabelle muss angegeben werden!

#b.
INSERT INTO kunden ('vorname') VALUES ('Herbert');
# Lösung
INSERT INTO kunden (vorname) VALUES ('Herbert');
# Keine Gänsefüsschen nötig, weil es kein Datensatz ist!

#c.
INSERT INTO kunden (nachname, vorname, wohnort, land_id) VALUES ('Schulter', 'Albert', 'Duisburg', 'Deutschland');
# Lösung
INSERT INTO kunden (nachname, vorname, land_id, wohnort) VALUES ('Schulter', 'Albert', 4, "Duisburg");
# Reihenfolge muss übereinstimmen! Ausserdem ist land_id ein Integer, weshalb dort eine Zahl hin muss.

#d.
INSERT INTO kunden ('', 'Brunhild', 'Sulcher', 1, 'Süderstade');
# Lösung
INSERT INTO kunden  VALUES ('', 'Brunhild', 'Sulcher', 1, 'Süderstade');
# Syntaxfehler, VALUES ist nötig.

#e.
INSERT INTO kunden VALUES ('Jochen', 'Schmied', 2, 'Solingen');
# Lösung
INSERT INTO kunden VALUES (NULL, 'Jochen', 'Schmied', 2, 'Solingen');
# Die ID muss auch drinn sein. Auf NULL setzen. 

#f.
INSERT INTO kunden VALUES ('', 'Doppelbrecher', 2, '');
# Lösung
INSERT INTO kunden VALUES (NULL, '', 'Doppelbrecher', 2, '');
# ID fehlt

#g.
INSERT INTO kunden (nachname, wohnort, land_id) VALUES ('Christoph', 'Fesenkampp', 'Duisburg', 3);
# Lösung
INSERT INTO kunden (nachname, wohnort, land_id) VALUES ('Christoph', 'Fesenkampp', 3);
# Zu viele Daten angegeben

#h.
INSERT INTO kunden (vorname) VALUES ('Herbert');
# Lösung
INSERT INTO kunden (vorname) VALUES ('Herbert');
# Dieser Befehl funktioniert einwandfrei.

#i.
INSERT INTO kunden (nachname, vorname, wohnort, land_id) VALUES (Schulter, Albert, Duisburg, 1);
# Lösung
INSERT INTO kunden (nachname, vorname, wohnort, land_id) VALUES ("Schulter", "Albert", "Duisburg", 1);
# Gänsefüsschen vergessen

#j.
INSERT INTO kunden VALUE ('', "Brunhild", "Sulcher", 1, "Süderstade");
# Lösung
INSERT INTO kunden VALUES (NULL, "Brunhild", "Sulcher", 1, "Süderstade");
# S nach VALUE vergessen, NULL muss im ersten Feld stehen

#k.
INSERT INTO kunden VALUE ('', 'Jochen', 'Schmied', 2, Solingen);
# Lösung 
INSERT INTO kunden VALUE (NULL, 'Jochen', 'Schmied', 2, "Solingen");
# Gänsefüsschen vergessen, S nach VALUE, NULL im ersten Feld