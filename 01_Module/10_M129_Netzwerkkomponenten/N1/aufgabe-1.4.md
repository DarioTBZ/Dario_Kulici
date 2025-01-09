# N1 Aufgabenstellung 1.4

### Vorgaben
- IP Range vom ISP: 170.11.83.0/26
- Fehlerkorrektur 

### Fehlersuche

Die beste Methode bei der Fehlersuche in einem Netzwerk ist von Layer 1 bis Layer 4 zu suchen. Das heisst das erste was man macht ist das Kabel überprüfen usw. 

| Gerät  | Gefundener Fehler, ausgeführte Korrektur                                            |
| ------ | ----------------------------------------------------------------------------------- |
| Router | Interface 4 falsche IP-Adresse, von 170.11.83.27 auf 170.11.83.25 geändert.         |
| Router | Interface 7 falsche Subnetzmaske, von 255.255.252.248 auf 255.255.255.248 geändert. |
| PC-03  | Falscher Gateway, von 170.11.82.1 auf 170.11.83.1 geändert.                         |
| PC-10  | Falscher Gateway, von 170.11.83.8 auf 170.11.83.9 geändert.                         |
| PC-10  | Falsche IP-Adresse, von 170.11.83.11 auf 170.11.83.10 geändert.                     |
| PC-27  | Falscher Gateway, von 107.11.83.25 auf 170.11.83.25 geändert.                       |
| PC-43  | Kein Gateway, auf 170.11.83.41 geändert.                                            |
| PC-50  | Falsche IP-Adresse, von 170.11.83.250 auf 170.11.83.50 geändert.                    |
| PC-51  | Falsche Subnetzmaske, von 255.255.248.0 auf 255.255.255.248 geändert.               |
| PC-59  | Falscher Gateway, von 170.11.83.59 auf 170.11.83.57 geändert.                       |

### Pingtest
<img width=50% height=50% alt="Pingtest" src="">

Als letzter Schritt überprüfte ich ob der Ping in alle Netzwerke funktionierte. 