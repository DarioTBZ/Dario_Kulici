# Cloud-Migration für ein KMU

### Ausgangslage
50 Mitarbeiter arbeiten On-premise. Monatliche Kosten setzen sich aus mehreren Faktoren zusammen, darunter ein NAS Speicher von 20 TB. Die Hardware wird innerhalb von 3 Jahren abgeschrieben. 

Ist eine Migration zur AWS-Cloud sinnvoll und wie viel Geld wird gespart? Die Preise werden auf 3 Jahre hochgerechnet. 

#### On-Premise Kosten pro Monat

| **Kostenart**                |  **Betrag** |
| :--------------------------- | ----------: |
| Raummiete                    |     1'000.- |
| Administration (20% Stelle)  |     1'000.- |
| Server (HPE Proliant)        |     2'500.- |
| Netzwerk und weitere Geräte  |     2'500.- |
| Diverses (Lizenzen etc.)     |     2'500.- |
| **Gesamtkosten On-Premises** | **9'500.-** |
#### Low Variante pro Monat

| **Kostenart**               |     **Betrag** |
| :-------------------------- | -------------: |
| AWS EC2 t2.micro\*          |       211.70.- |
| AWS S3 Speicher 20 TB       |          471.- |
| Administration (20% Stelle) |        1'000.- |
| Diverses (Lizenzen etc.)    |        2'500.- |
| **Gesamtkosten AWS Low**    | **4'182.70.-** |

\*Es wurden Linux Instanzen ausgewählt, da es kein Windows Betriebssystem an sich als Variante gab. 

#### X-Large Variante pro Monat

| **Kostenart**               |     **Betrag** |
| :-------------------------- | -------------: |
| AWS EC2 m4.xlarge\*         |     3'628.10.- |
| AWS S3 Speicher 20 TB       |          471.- |
| Administration (20% Stelle) |        1'000.- |
| Diverses (Lizenzen etc.)    |        2'500.- |
| **Gesamtkosten AWS Low**    | **7’599.10.-** |

\*Es wurden Linux Instanzen ausgewählt, da es kein Windows Betriebssystem an sich als Variante gab. 

#### Vergleichstabelle Varianten

| Variante   | Pro Monat  | Pro Jahr    | 3 Jahre      |
| ---------- | ---------- | ----------- | ------------ |
| On-Premise | 9'500      | 114'000.-   | 342'000.-    |
| t2.micro   | 4'182.70.- | 50'192.40.- | 150’577.20.- |
| m4.xlarge  | 7'599.70.- | 91'196.40.- | 273’589.20.- |
#### Vor- und Nachteile der Cloud

##### Vorteile:
- Weniger Kosten
- Flexibler Arbeitsort
- Einfache Skalierung
- Kein Wartungsaufwand

##### Nachteile:
- Höhere Latenz als On-Premise
- Weniger Kontrolle
- Datenschutzbedenken
- Leistungsschwankungen

#### Lösungsvorschlag
Preislich ist es klar, dass sich das Arbeiten in der Cloud mehr lohnt als on Premise zu arbeiten. Jetzt bleibt nur noch zu entscheiden ob man die Low oder Large Variante auswählt. Es kommt sehr drauf an, was man auf den Instanzen arbeitet. Bei Arbeiten, die wenig Leistung benötigen und keine grafisch aufwendige Grafiken rendern müssen, empfehle ich die Low Variante. Bei leistungsaufwendigeren Arbeiten wie z.B Designen oder Virtuelle Maschinen empfehle ich die Large Variante.

Wenn man mit simplen Texttools und Webapplikationen arbeitet ist die Low Variante am besten. Sonst lohnt sich die Large Variante. Je nach dem, was das Unternehmen macht, kann man sich so für eine der zwei Varianten entscheiden. 