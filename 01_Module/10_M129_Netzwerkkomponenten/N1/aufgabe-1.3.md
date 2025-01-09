# N1 Aufgabenstellung 1.3

### Vorgaben 
- IP Range vom ISP: 25.30.120.0/26
- Vier gleich grosse Subnetze
- Namenskonvention

### Netzwerk Konfiguration
Für vier gleich grosse Subnetze in der Range vom ISP braucht es ein /28er Netz mit je 16 Adressen pro Subnetz. 

Netzteil: 28

Hostteil: 4


| Subnetz ID | Netzwerk ID  | Verfügbare Adressen | Besetzte Adressen | Freie Adressen |
| ---------- | ------------ | ------------------- | ----------------- | -------------- |
| 1          | 25.30.120.0  | 16                  | 3                 | 11             |
| 2          | 25.30.120.16 | 16                  | 3                 | 11             |
| 3          | 25.30.120.32 | 16                  | 3                 | 11             |
| 4          | 25.30.120.48 | 16                  | 3                 | 11             |

Nur der Router und zwei PC's pro Subnetz brauchen IP-Adressen. 

#### Netzwerk 1
<img width=50% height=50% alt="Netzwerk1" src="https://github.com/user-attachments/assets/70db611c-54a0-41c6-b99f-90bc7e2bd7bd">

#### Netzwerk 2
<img width=50% height=50% alt="Netzwerk2" src="https://github.com/user-attachments/assets/4dd0cf24-a16b-43ef-b410-d8bde7a9d945">

#### Netzwerk 3
<img width=50% height=50% alt="Netzwerk3" src="https://github.com/user-attachments/assets/91272eb5-c9f0-4855-ae14-9284c79a33b0">

#### Netzwerk 4
<img width=50% height=50% alt="Netzwerk4" src="https://github.com/user-attachments/assets/fa97c2a6-7c01-4777-b7e1-567a63ecba0c">

### PC Konfiguration

| ID  | Name  | IP-Adresse   | CIDR |
| --- | ----- | ------------ | ---- |
| 1   | PC-2  | 25.30.120.2  | 28   |
| 2   | PC-3  | 25.30.120.3  | 28   |
| 3   | PC-18 | 25.30.120.18 | 28   |
| 4   | PC-19 | 25.30.120.19 | 28   |
| 5   | PC-34 | 25.30.120.34 | 28   |
| 6   | PC-35 | 25.30.120.35 | 28   |
| 7   | PC-50 | 25.30.120.50 | 28   |
| 8   | PC-51 | 25.30.120.51 | 28   |


<img width=50% height=50% alt="PCconfig" src="https://github.com/user-attachments/assets/87842bdd-6af5-4417-a46f-6014fbfff518">
Auf diesem Bild sieht man die Konfiguration von PC-2. 

Der Gateway und die Netzmaske sind die Felder, die gleich bleiben. Die IP ändert sich von PC zu PC. 

<img width=50% height=50% alt="Pingtest" src="https://github.com/user-attachments/assets/d4efd72f-dc4e-4b68-afe2-1634d89762ec">

Um zu beweisen, dass das Netz funktioniert hier ein Bild. 

### Fragen 
- Wieviele freie IP-Adressen gibt es in der Abteilung **Buchhaltung**.
- Ist ein mögliches Wachstum der Firma berücksichtigt?
- Ist das Netzwerk-Design sinnvoll?
- Gibt es Verbesserungsvorschläge bzgl. Netzwerk-Design?
- Welche zusätzlichen Informationen wären nützlich, um für dieses Netzwerk-Design einen Optimierungsvorschlag auszuarbeiten?

### Antworten
- Die Abteilung Buchhaltung hat 11 freie IP-Adressen. 
- Grundsätzlich schon, weil noch freie IP-Adressen verfügbar sind. 
- Ja, jede Abteilung hat ihr Subnetz und alles ist ordentlich gegliedert. 
- Nein. Für eine simple Firma ist das ein gutes Netzwerk. 
- Wie viel Mitarbeiter pro Jahr neu in die Firma kommen. 
