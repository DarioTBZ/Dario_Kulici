# N3 Aufgabenstellung 3.2

### Vorgaben
- Fehlersuche in 4 Netzwerken

### Netzwerkanalyse
Ich gehe wieder so vor, dass ich zuerst Layer 1, dann Layer 2 und als letztes Layer 3 analysiere und nach Fehler finde. Es bringt nichts eine funktionierende Konfiguration auf Layer 3 zu haben und dann sind die Geräte nicht mal eingesteckt. 

### Fehlerdokumentation

| Filename              | Fehlerbeschrieb                                                                      |
| --------------------- | ------------------------------------------------------------------------------------ |
| Netzwerk-Fehler-1.fls | NB-4-1 und NB-4-2 können nicht mit NBs in anderen Netzwerken kommunizieren.          |
| Netzwerk-Fehler-2.fls | NB-4-1 und NB-3-2 konnten nicht mit anderen NBs in anderen Netzwerken kommunizieren. |
| Netzwerk-Fehler-3.fls |                                                                                      |
| Netzwerk-Fehler-4.fls |                                                                                      |


| Filename              | Gefundener Fehler, ausgeführte Korrektur                                                                              |
| --------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Netzwerk-Fehler-1.fls | NB-4-1 und NB-4-2 hatten keinen Gateway hinterlegt, Gateway auf 192.168.4.1 geändert.                                 |
| Netzwerk-Fehler-2.fls | Das falsche Interface auf dem Router war zum Switch verbunden, richtiges Interface (192.168.3.1) zu SW-3-1 verbunden. |
| Netzwerk-Fehler-3.fls |                                                                                                                       |
| Netzwerk-Fehler-4.fls |                                                                                                                       |


| Ausgeführter Test               | Beobachtetes Resultat                                    |
| ------------------------------- | -------------------------------------------------------- |
| Überprüfung der Konfigurationen | Falsche Konfiguration, Konfiguration angepasst           |
| Ping zu allen Netzwerken        | Ping fehlgeschlagen, --> Überprüfung der Konfigurationen |
