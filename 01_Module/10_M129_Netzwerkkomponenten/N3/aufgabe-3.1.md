# N3 Aufgabenstellung 3.1

### Vorgaben
- Fehlersuche in 4 Netzwerken

### Netzwerkanalyse
Die beste Technik, um Fehler im Netzwerk herausfindig zu machen ist sich die **ISO/OSI Layers** hinauf zu arbeiten. Beginnend bei der Verkabelung der Geräte (Layer 1), zu der Funktionalität der Switches (Layer 2) zur IP-Konfiguration der Geräte (Layer 3). 

| Filename              | Fehlerbeschrieb                                             |
| --------------------- | ----------------------------------------------------------- |
| Netzwerk-Fehler-1.fls | PC_NW1_4 kann nicht mit anderen PCs kommunizieren (ping).   |
| Netzwerk-Fehler-2.fls | PC_NW1_4 kann nicht mit anderen PCs kommunizieren (ping).   |
| Netzwerk-Fehler-3.fls | PC_NW1_1 kann nicht mit anderen PCs kommunizieren (ping).   |
| Netzwerk-Fehler-4.fls | NW3 kann nicht mit anderen Netzwerken kommunizieren (ping). |
| Netzwerk-Fehler-5.fls |                                                             |

| Filename              | Gefundener Fehler, ausgeführte Korrektur                                                                  |
| --------------------- | --------------------------------------------------------------------------------------------------------- |
| Netzwerk-Fehler-1.fls | Subnetzmaske von PC_NW1_4 von 255.255.255.0 auf 255.255.255.192 geändert.                                 |
| Netzwerk-Fehler-2.fls | Gateway von PC_NW1_4 von 192.168.1.2 auf 192.168.1.1 geändert.                                            |
| Netzwerk-Fehler-3.fls | IP-Adresse von PC_NW1_1 von 169.254.1.1 auf 192.168.1.11 geändert.                                        |
| Netzwerk-Fehler-4.fls | Router IP-Table Subnetzmaske von 255.255.255.252 auf 255.255.255.192 für Netzwerk 192.168.1.128 geändert. |
| Netzwerk-Fehler-5.fls |                                                                                                           |