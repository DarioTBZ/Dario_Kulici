# Block 4

# Liste aller Produkte
# Liste aller Kategorien
# Liste aller Kunden. Geben Sie nur Vorname, Nachname und Emailadresse aus
# Liste aller Bestellungen sortiert nach Bestelldatum
# Liste aller Produkte absteigend sortiert nach Preis
# Liste der teuersten 3 Produkte
# Liste der günstigsten 3 Produkte

SELECT * FROM product;
SELECT * FROM category;
SELECT firstname, lastname, email FROM customer;
SELECT * FROM order_entry ORDER BY ordered_at;
SELECT * FROM product ORDER BY price DESC;
SELECT * FROM product ORDER BY price DESC LIMIT 3;
SELECT * FROM product ORDER BY price LIMIT 3;

# Block 5

# Berechnen Sie die Quadratwurzel aller Produktpreise.
# Geben Sie den Namen des Monats aus dem Datum der Bestellungen aus.
# Zählen Sie die Anzahl Buchstaben in den Vornamen der Kunden.
# Liste der Email Adressen aller Kunden. Teilen Sie die Adresse in zwei Spalten auf Account und Domain.
# z.B. hans@muster.com: hans, muster.com
# Geben Sie die Initialen der Kunden in einer Spalte aus.
# z.B. Hans Muster: HM
# Berechnen Sie die 8% Mehrwertsteuer, die in den Preisen inbegriffen ist (Optional: Runden Sie die MwSt auf 5 Rappen)
# Geben Sie die Anzahl Datensätze ihrer Produkttabelle aus.
# Berechnen Sie Mindest-, Höchst- und Durchschnittspreis aller Produkte

SELECT
sqrt(price) as square_root 
FROM product;

SELECT month(ordered_at) AS Month
FROM order_entry;

SELECT firstname AS Vorname, length(firstname) AS Länge FROM customer;

SELECT
 email,
 substring_index(email, '@', 1) as Account,
 substring_index(email, '@', -1) as Domain
FROM customer;

SELECT 
	firstname,
    lastname,
    concat(LEFT(firstname, 1), LEFT(lastname, 1)) AS Initialen
FROM customer;

SELECT 
	price,
    price * 0.08 AS Mehrwertsteuer
FROM product;

SELECT count(*) FROM customer;

# 4.3 

SELECT * 
FROM product
WHERE id = 5;

SELECT * 
FROM product
WHERE id < 3;

SELECT * 
FROM product
WHERE id < 3 
OR
id > 8;

SELECT * FROM product 
WHERE id = 1
OR id = 3
OR id = 5
OR id = 7;

