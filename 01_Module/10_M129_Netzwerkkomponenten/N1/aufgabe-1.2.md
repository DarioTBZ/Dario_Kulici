# N1 Aufgabenstellung 1.2

### Vorgaben
- IP Range vom ISP: 59.136.34.0/24
- Acht gleichgrosse Subnetze (eins für jede Abteilung)


### Netzwerk Konfiguration
Für acht gleichgrosse Netze braucht es ein /27er Netzwerk. 

Netzbits: 27

Hostbits: 5

5 + 27 = 32 Bits = volle IP Adresse


Ein 27er Netz hat 8 Subnetze mit je 32 Adressen, davon **30 nutzbar von Hosts**. Das heisst die Subnetze sind folgendermassen aufgebaut.

| Subnetz ID | Netzwerk ID   | Netzanteil | Hostanteil |
| ---------- | ------------- | ---------- | ---------- |
| 1          | 59.136.34.0   | 2          | 30         |
| 2          | 59.136.34.32  | 2          | 30         |
| 3          | 59.136.34.64  | 2          | 30         |
| 4          | 59.136.34.96  | 2          | 30         |
| 5          | 59.136.34.128 | 2          | 30         |
| 6          | 59.136.34.160 | 2          | 30         |
| 7          | 59.136.34.192 | 2          | 30         |
| 8          | 59.136.34.224 | 2          | 30         |


#### Netzwerk 1
<img width=50% height=50% alt="01_subnetzconfig" src="https://github.com/user-attachments/assets/fda2da36-fab4-4c27-accc-712e82037e97">

Netzwerk ID: 59.136.34.0

Erste IP: 59.136.34.1

Letzte IP: 59.136.34.30

Broadcast: 59.136.34.31

#### Netzwerk 2
<img width=50% height=50% alt="02_subnetzconfig_2" src="https://github.com/user-attachments/assets/a63caa9c-ccd7-4b02-b552-6b92dc5f2f47">

Netzwerk ID: 59.136.34.32

Erste IP: 59.136.34.33

Letzte IP: 59.136.34.62

Broadcast: 59.136.34.63

Hier verändern sich die 3 Bits im vierten Quartett. Da müssen die Bits einfach an der Netzwerk ID angepasst werden. Also hier im Bild eine 1 bei 32, weil die Netzwerk ID 32 ist. Im letzten Subnetz sind **alle 3 Netz Bits im vierten Oktett 1**. 

#### Netzwerk 6
<img width=50% height=50% alt="03_subnetzconfig_6" src="https://github.com/user-attachments/assets/a555930e-bf1d-4e2c-88da-93ed43c6fa1f">

Netzwerk ID: 59.136.34.160

Erste IP: 59.136.34.161

Letzte IP: 59.136.34.190

Broadcast: 59.136.34.191

Ich zeige nicht alle Netzwerke im Excel auf dieser Dokumentation, sondern nur genug um mein Verständnis und die Richtigkeit zu vermitteln. 

Auf diesem Bild von Netzwerk 6 sieht man, dass nicht je höher das Subnetz desto mehr Bits, sondern es variiert stark. 160 besteht aus 128 und 64, weswegen dort je eine 1 ist. 

### Umsetzung
Acht Subnetze konfigurieren ist ganz schön viel. Deswegen ist es gut alles in einem Excel vorgeplant zu haben. So musste ich nur noch vom Excel abschauen und die Konfiguration anpassen. 

<img width=50% height=50% alt="Routerconfig" src="https://github.com/user-attachments/assets/389bc106-71a8-4d19-8e31-4fe73e1e0858">

Als erstes habe ich immer ein Interface vom Router genommen und es mit der Router IP, also die erste im Subnetz, z.B 59.136.34.1. 

<img width=50% height=50% alt="PCconfig" src="https://github.com/user-attachments/assets/e7863cd6-9984-4531-baf4-ec7ebead47d9">

Als nächstes nahm ich beide PCs und gab ihnen, die vorgeschriebenen IP-Adressen. Auf dem Bild ist PC-10 mit der IP 59.136.34.10. Da musste ich nur die Subnetzmaske anpassen und den Gateway auf den Router zeigen lassen, damit die Kommunikation festgelegt war. 

<img width=50% height=50% alt="Configtest" src="https://github.com/user-attachments/assets/041ad205-6e4b-4b32-b43b-ab7b70a58619">

Nachdem Abschluss von **einem Subnetz** pingte ich vom einen PC den anderen und schaute ob der Ping ankam (und wieder zurück). Das gelang mir zu 100% ohne grosse Schwierigkeiten. 


### Fazit

Mein Filius Programm auf meinem Heim PC hatte verrückte Grafikfehler während ich die Aufgabe erledigte, aber es ging noch so. Hier ein Video zum Verständnis. 

PlaceholderVideo
