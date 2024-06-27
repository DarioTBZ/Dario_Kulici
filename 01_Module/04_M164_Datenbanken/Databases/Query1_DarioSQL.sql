INSERT INTO address(person_address, fk_location_id) VALUES
("Bomboclatstrasse 7", 1);

INSERT INTO location(location, postal_code) VALUES
("Zürich Hardbrücke", "8005"),
("Buchs", "8105");

SELECT * from beispiel_preis;

UPDATE beispiel SET beispielname = "text" WHERE id = 1;

UPDATE address SET person_address = "Bomboaclatstrasse 8" WHERE id = 2;

UPDATE beispiel SET beispiel_text = "neuer text", beispiel_text_2 = "nochmal bearbeitet";

UPDATE beispiel_preis SET price = price * 2; # ändert den Preis von ALLEN Einträgen von Beispielpreis

CREATE TABLE beispiel_preis ( 
	price INT UNSIGNED NOT NULL
	);
    
DELETE FROM beispiel_table WHERE id = 1; 
DELETE FROM `table`; # löscht alles vom table

SELECT price AS "Produktname", price AS "Preis" FROM product; # Attribut name als "Produktname" und price als "Preis" anzeigen lassen

SELECT * FROM beispiel_table WHERE id = 1; # anzeigen wo die ID 1 ist

SELECT * FROM beispiel_table WHERE id = 1 OR id = 2; # Zeigt Attribute von den IDs 1 und 2


SELECT * FROM product ORDER BY price DESC, `name`; # nacheinander sortieren

select price as "Preis", product_name as "Name" from beispiel_preis;

insert into beispiel_preis(price, product_name) values
(1, "Banane"),
(2, "Apfel"),
(3, "Schachtel");

SELECT
count(*) 
FROM price



create schema pizza_express;