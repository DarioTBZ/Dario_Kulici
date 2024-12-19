# Aufgabenstellung 1.1

### Vorgaben
- IP Range von ISP: 160.160.250.0 /24
- Für die Abteilungen zwei gleichgrosse Subnetze
- Erste Subnetz IP ist für Router reserviert
- Clients können die erste IP nach dem Router nutzen. 
- Namenskonvention

### Netzwerke
Damit das Netzwerk in zwei geteilt werden kann erstelle ich **zwei /25er** Netze. Jede Abteilung hat 255 IP Adressen und total sind es 512 IP Adressen. 



**Netzwerk ID's**
Netzwerk 1: 160.160.250.0
Netzwerk 2: 160.160.251.0

#### Netzwerk 1

<img width=50% height=50% alt="network-1" src="https://github.com/user-attachments/assets/72a7a2bf-bb81-47af-bbbc-960b5afe4ba1">

Router IP: 160.160.250.1

Letzte IP: 160.160.250.254

Anzahl IP Adressen für PC's: 253

#### Netzwerk 2

<img width=50% height=50% alt="network-2" src="https://github.com/user-attachments/assets/865aaa79-1bbd-4596-97cb-f27feb53feaa">

Router IP: 160.160.251.1

Letzte IP: 160.160.251.254

Anzahl IP Adressen für PC's: 253
