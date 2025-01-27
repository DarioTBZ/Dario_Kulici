#a.	Lassen Sie sich mit SELECT alle Datensätze Ihrer DVD-Sammlung ausgeben.
SELECT * FROM dvd_sammlung;
#b Erstellen Sie eine Anweisung, die alle Filmtitel und die jeweils zugehörige Nummer ausgibt.
SELECT film, nummer FROM dvd_sammlung;
#c.	Erstellen Sie eine Anweisung, die alle Filmtitel und den jeweils zugehörigen Regisseur ausgibt.
SELECT film, regisseur FROM dvd_sammlung;
#d.	Erstellen Sie eine Liste mit allen Filmen von Quentin Tarantino.
SELECT * FROM dvd_sammlung WHERE regisseur = "Quentin Tarantino";
#e.	Erstellen Sie eine Liste mit allen Filmen von Steven Spielberg.
SELECT * FROM dvd_sammlung WHERE regisseur = "Steven Spielberg";
#f.	Erstellen Sie eine Liste aller Filme, in denen der Regisseur den Vornamen "Steven" hat.
SELECT * FROM dvd_sammlung WHERE regisseur LIKE "Steven%";
#g.	Erstellen Sie eine Liste mit allen Filmen, die länger als 2 Stunden sind.
SELECT * FROM dvd_sammlung WHERE laenge_minuten > 120;
#h.	Erstellen Sie eine Liste mit allen Filmen, die von Tarantino oder von Spielberg gedreht wurden.
SELECT * FROM dvd_sammlung WHERE regisseur = "Quentin Tarantino" OR regisseur = "Steven Spielberg";
#i.	Suchen Sie alle Filme heraus, die von Tarantino gedreht wurden und kürzer als 90 Minuten sind.
SELECT * FROM dvd_sammlung WHERE regisseur = "Quentin Tarantino" AND laenge_minuten < 90;
#j.	Sie erinnern sich an einen Film, in dessen Titel "Sibirien" vorkam. Suchen Sie ihn.
SELECT * FROM dvd_sammlung WHERE film LIKE "%Sibirien%";
#k.	Lassen Sie sich alle Teile von "Das große Rennen" ausgeben.
SELECT * FROM dvd_sammlung WHERE film LIKE "%Das große Rennen%";
#l.	Lassen Sie sich eine Liste aller Filme ausgeben, sortiert nach Regisseur.
SELECT film, regisseur FROM dvd_sammlung ORDER BY regisseur;
#m.	Lassen Sie sich eine Liste aller Filme ausgeben, sortiert nach Regisseur, dann nach Filmtitel.
SELECT film, regisseur FROM dvd_sammlung ORDER BY regisseur, film;
#n.	Lassen Sie sich eine Liste aller Filme von Tarantino ausgeben, die längsten zuerst.
SELECT * FROM dvd_sammlung WHERE regisseur = "Quentin Tarantino" ORDER BY laenge_minuten DESC;