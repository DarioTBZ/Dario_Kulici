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

| Subnetz ID | Netzwerk ID   | Verfügbare Adressen | Besetzte Adressen | Freie Adressen |
| ---------- | ------------- | ------------------- | ----------------- | -------------- |
| 1          | 59.136.34.0   | 30                  | 3                 | 27             |
| 2          | 59.136.34.32  | 30                  | 3                 | 27             |
| 3          | 59.136.34.64  | 30                  | 3                 | 27             |
| 4          | 59.136.34.96  | 30                  | 3                 | 27             |
| 5          | 59.136.34.128 | 30                  | 3                 | 27             |
| 6          | 59.136.34.160 | 30                  | 3                 | 27             |
| 7          | 59.136.34.192 | 30                  | 3                 | 27             |
| 8          | 59.136.34.224 | 30                  | 3                 | 27             |

Der Router und zwei PC's pro Subnetz sind die Geräte die eine IP-Adresse brauchen. Die restlichen 27 sind frei. 

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

#### PC's Konfiguration

| ID  | Name   | IP-Adresse    | CIDR |
| --- | ------ | ------------- | ---- |
| 1   | PC-10  | 59.136.34.10  | 27   |
| 2   | PC-20  | 59.136.34.20  | 27   |
| 3   | PC-40  | 59.136.34.40  | 27   |
| 4   | PC-50  | 59.136.34.50  | 27   |
| 5   | PC-70  | 59.136.34.70  | 27   |
| 6   | PC-80  | 59.136.34.80  | 27   |
| 7   | PC-110 | 59.136.34.110 | 27   |
| 8   | PC-120 | 59.136.34.120 | 27   |
| 9   | PC-130 | 59.136.34.130 | 27   |
| 10  | PC-140 | 59.136.34.140 | 27   |
| 11  | PC-170 | 59.136.34.170 | 27   |
| 12  | PC-180 | 59.136.34.180 | 27   |
| 13  | PC-200 | 59.136.34.200 | 27   |
| 14  | PC-210 | 59.136.34.210 | 27   |
| 15  | PC-230 | 59.136.34.230 | 27   |
| 16  | PC-240 | 59.136.34.240 | 27   |
### Formative Fragen
- Wieviele freie IP-Adressen gibt es in der Abteilung **Einkauf**
- Wo liegt die Grenze bzgl. Zuweisung der IPs an Mitarbeiter? (Pro Abteilung)
- Ist dieses Netzwerk-Design realistisch? (Kritische Begründung)
- Gibt es Verbesserungsvorschläge bzgl. Netzwerk-Design?
-  Welche zusätzlichen Informationen wären nützlich, um für dieses Netzwerk-Design einen Optimierungsvorschlag auszuarbeiten?

- In der Abteilung Einkauf sind so wie in jeder Abteilung noch 27 IP-Adressen frei.
- Es können nicht mehr als 30 Mitarbeiter pro Abteilung arbeiten, weil es keine IP-Adressen mehr hat. 
- Nein, weil zu wenig Adressen genutzt werden, also es somit Verschwendung ist und der Verwaltungsaufwand wäre zu gross. 
- Wie viele Geräte es hat, die eine IP-Adresse brauchen und ob man erwartet, dass das Netzwerk wächst. 

### Fazit

Mein Filius Programm auf meinem Heim PC hatte verrückte Grafikfehler während ich die Aufgabe erledigte, aber es ging noch so. Hier ein Video zum Verständnis. 

https://github.com/user-attachments/assets/ff693cc4-bd1c-41df-ae25-a36f591cb07b

