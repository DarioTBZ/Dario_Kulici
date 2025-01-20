# N2 Aufgabenstellung 2.4

### Vorgaben
- IP Range von ISP: 133.95.48.0/23
- Vier gleich grosse Subnetze

### Netzwerk
Der ISP stellt ein /23er Netz zur Verfügung. Es sollen vier gleich grosse Netzwerk erstellt werden. Dafür ist ein /25er Netz perfekt. Pro Subnetz sind 128 IP-Adressen inkludiert. 

| Subnetz ID | Netzwerk ID   | Verfügbare Adressen | Besetzte Adressen | Freie Adressen | Abteilung   |
| ---------- | ------------- | ------------------- | ----------------- | -------------- | ----------- |
| 1          | 133.95.48.0   | 126                 | 3                 | 123            | GL          |
| 2          | 133.95.48.128 | 126                 | 3                 | 123            | Buchhaltung |
| 3          | 133.95.49.0   | 126                 | 3                 | 123            | Verkauf     |
| 4          | 133.95.49.128 | 126                 | 3                 | 123            | Einkauf     |

Die besetzten IP-Adressen sind die des **Routers und der zwei PCs** pro Subnetz. 

### Excel Netzwerktabelle
Wichtig ist hier im dritten Oktett ein Bit umzuschalten. Das heisst das dritte Oktett wechselt von 48 auf 49. 

<img width=50% height=50% alt="Netzwerk3und4" src="https://github.com/user-attachments/assets/0c099c35-13a5-4c57-9e29-de24e53642e1">

### PC Konfiguration
Hier sieht man die Konfiguration der PCs. Es ändert sich lediglich der **Gateway und ein wenig die IP-Adresse**. 

<img width=50% height=50% alt="PCconfig-ip" src="https://github.com/user-attachments/assets/1d66f6d0-df78-4664-a192-7242e9f35961">

<img width=50% height=50% alt="PCconfig" src="https://github.com/user-attachments/assets/ad0f59f5-7e4c-4b50-bedc-cc3d2d89a9e4">

#### IP-Vergebung PCs

| ID  | Name    | IP-Adresse    | CIDR |
| --- | ------- | ------------- | ---- |
| 1   | PC-8050 | 133.95.48.50  | 25   |
| 2   | PC-8080 | 133.95.48.80  | 25   |
| 3   | PC-8130 | 133.95.48.130 | 25   |
| 4   | PC-8140 | 133.95.48.140 | 25   |
| 5   | PC-9050 | 133.95.49.50  | 25   |
| 6   | PC-9080 | 133.95.49.80  | 25   |
| 7   | PC-9130 | 133.95.49.130 | 25   |
| 8   | PC-9140 | 133.95.49.140 | 25   |


### Testing

Wie immer waren die ersten PDUs nicht erfolgreich. Sobald der Router die ARP Tabelle ausgefüllt hat konnte ich erfolgreich pingen und PDUs senden. 

<img width=50% height=50% alt="TestingPDU" src="https://github.com/user-attachments/assets/9cddf268-9457-4255-9b85-fbab24144451">

<img width=50% height=50% alt="TestingPing" src="https://github.com/user-attachments/assets/7c8322d2-21ac-4326-8eca-f686025d76e7">

### Fragen
- Wieviele freie IP-Adressen gibt es in der Abteilung **Einkauf**
- Ist ein mögliches Wachstum der Firma berücksichtigt?
- Ist das Netzwerk-Design sinnvoll?
- Gibt es Verbesserungsvorschläge bzgl. Netzwerk-Design?
- Welche zusätzlichen Informationen wären nützlich, um für dieses Netzwerk-Design einen Optimierungsvorschlag auszuarbeiten?

### Antworten
- In der Abteilung Einkauf sind 123 freie IP-Adressen
- Ja es ist berücksichtigt, denn es gibt genug freie IP-Adressen in jeder Abteilung
- Ja durchaus. Alles Abteilungen sind getrennt und übersichtlich. 
- Wie schon in anderen Aufgaben ist hier ein Single Point of Failure. Das heisst wenn der Router ausfällt kann keiner mehr arbeiten.
- Ob genug Budget für eine Umstrukturierung vorhanden ist. 
