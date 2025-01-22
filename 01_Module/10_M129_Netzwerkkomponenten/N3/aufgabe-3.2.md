# N3 Aufgabenstellung 3.2

### Vorgaben
- Fehlersuche in 4 Netzwerken

### Netzwerkanalyse
Ich gehe wieder so vor, dass ich zuerst Layer 1, dann Layer 2 und als letztes Layer 3 analysiere und nach Fehler finde. Es bringt nichts eine funktionierende Konfiguration auf Layer 3 zu haben und dann sind die Geräte nicht mal eingesteckt. 

### Fehlerdokumentation

| Filename              | Fehlerbeschrieb                                                             |
| --------------------- | --------------------------------------------------------------------------- |
| Netzwerk-Fehler-1.fls | NB-4-1 und NB-4-2 können nicht mit NBs in anderen Netzwerken kommunizieren. |
| Netzwerk-Fehler-2.fls | Kommunikation zwischen Netz 1 und 2 zu Netz 3 und 4 schlägt fehl.           |
| Netzwerk-Fehler-3.fls | Kommunikation zwischen Netz 1 und 2 zu Netz 3 und 4 schlägt fehl.           |
| Netzwerk-Fehler-4.fls | Netz 1 und 2 können nicht mit den Netzen 3 und 4 kommunizieren.             |


| Filename              | Gefundener Fehler, ausgeführte Korrektur                                                                                                                                                                  |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Netzwerk-Fehler-1.fls | NB-4-1 und NB-4-2 hatten keinen Gateway hinterlegt, Gateway auf 192.168.4.1 geändert.                                                                                                                     |
| Netzwerk-Fehler-2.fls | Interfaces für die Kommunikation von RT-2 zu RT-3 auf RT-2 waren vertauscht + waren die Interfaces auf RT-2 zu Netz 3 falsch und es hatte ein zusätzliches Interface, was überhaupt nicht benötigt wurde. |
| Netzwerk-Fehler-3.fls | Auf RT-3 war der falsche Gateway gesetzt, von 192.168.2.1 auf 10.1.0.2 geändert.                                                                                                                          |
| Netzwerk-Fehler-4.fls | Statt Router bei Netz 1 und 2 war ein Switch platziert, Switch mit Router ersetzt und konfiguriert.                                                                                                       |


| Ausgeführter Test               | Beobachtetes Resultat                                    |
| ------------------------------- | -------------------------------------------------------- |
| Überprüfung der Konfigurationen | Falsche Konfiguration, Konfiguration angepasst           |
| Ping zu allen Netzwerken        | Ping fehlgeschlagen, --> Überprüfung der Konfigurationen |

