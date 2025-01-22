# N3 Aufgabenstellung 3.3

### Vorgaben
- Fehlersuche

### Fehlersuche

| Device              | Gefundener Fehler, ausgeführte Korrektur                                                                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Laptop 192.168.0.10 | Falsche Subnetzmaske und kein Gateway gesetzt, Subnetzmaske korrigiert und Gateway gesetzt.                                                                               |
| Laptop 192.168.0.20 | Falsche Subnetzmaske und kein Gateway gesetzt, Subnetzmaske korrigiert und Gateway gesetzt.                                                                               |
| Router 1            | Falsche IPs + Subnetzmaske gesetzt (beide Interfaces), Interface 1 auf 192.168.0.1 und Interface 2 auf 192.168.1.1 gesetzt. Gateway von Router auf 192.168.1.254 gesetzt. |
| Laptop 192.168.1.10 | Kein Gateway gesetzt, Gateway auf 192.168.1.1 gesetzt.                                                                                                                    |
| Router 2            | Falsche IP-Adressen auf beiden Interfaces, Interface 1 IP auf 192.168.1.254 und Interface 2 IP auf 192.168.2.1 gesetzt und richtige Subnetzmasken definiert.              |
| Laptop 192.168.2.10 | Falsche Subnetz + kein Gateway, Subnetz und Gateway gesetzt. (255.255.255.0 und 192.168.2.1)                                                                              |
| Laptop 192.168.2.20 | Falsche Subnetz + kein Gateway, Subnetz und Gateway gesetzt. (255.255.255.0 und 192.168.2.1)                                                                              |

| Ausgeführter Test        | Beobachtetes Resultat/ (ausgeführte Korrektur)                    |
| ------------------------ | ----------------------------------------------------------------- |
| Pingen in jedes Netzwerk | Fehlgeschlagen, Konfigurationen angepasst                         |
| ARP Tabelle füllen       | Durch das ganze Netzwerk gepingt, sodass jeder jedes Gerät kennt. |
