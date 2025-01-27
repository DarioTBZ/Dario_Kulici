# N1 Aufgabenstellung 1.1

### Vorgaben
- IP Range vom ISP: 160.160.250.0 /24
- Für die Abteilungen zwei gleich grosse Subnetze
- Erste Subnetz IP ist für Router reserviert
- Clients können die erste IP nach dem Router nutzen. 
- Namenskonvention

### Netzwerk Konfiguration
Damit das Netzwerk in zwei geteilt werden kann erstelle ich **zwei /25er** Netze. Jede Abteilung hat 128 IP Adressen und total sind es 255 IP Adressen. 

**Netzwerk ID's**
Netzwerk 1: 160.160.250.0
Netzwerk 2: 160.160.250.128

#### Netzwerk 1

<img width=50% height=50% alt="network-1" src="https://github.com/user-attachments/assets/319f1236-8553-40ee-a378-5c77bba3e31c">

Router IP: 160.160.250.1

Letzte IP: 160.160.250.126

Anzahl IP Adressen für PC's: 125

#### Netzwerk 2

<img width=50% height=50% alt="network-2" src="https://github.com/user-attachments/assets/1ad8642d-c88c-4529-bbbe-4c876a57a84f">

Router IP: 160.160.250.129

Erste IP: 160.160.250.130

Letzte IP: 160.160.250.254

Anzahl IP Adressen für PC's: 125

### Umsetzung
Hier ist eine visuelle Übersicht vom Netzwerk. 

<img width=50% height=50% alt="network-overview" src="https://github.com/user-attachments/assets/4090d468-5f59-4d52-bc1f-dc8c9e3bf9c0">

#### Router Konfiguration
<img width=50% height=50% alt="routerconfig" src="https://github.com/user-attachments/assets/3f09b989-970d-443c-94c1-9610b143fe05">

Auf dem Router sind zwei Interfaces mit den IP Adressen 160.160.250.1 und 160.160.250.129. Auf diese IP Adressen gehen die Hosts, um mit anderen Hosts zu kommunizieren. 

#### PC Konfiguration
<img width=50% height=50% alt="pc-01-config" src="https://github.com/user-attachments/assets/a814b45c-7858-4b22-93ad-b1933910980b">

Auf dem Bild ist PC-01 mit der ersten IP Adresse im Netzwerk. Der zweite PC hat die letzte IP Adresse. Hier eine Liste für eine bessere Übersicht. 

