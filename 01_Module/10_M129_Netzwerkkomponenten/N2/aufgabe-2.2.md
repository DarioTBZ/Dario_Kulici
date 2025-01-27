# N2 Aufgabenstellung 2.2

### Vorgaben
- IP Range vom ISP: 37.105.96.0/22
- Acht gleich grosse Subnetze

### Netzwerk
Der ISP stellt ein /22er Netz zur Verfügung und für den Auftrag wird das in ein /25er Netz aufgeteilt. Pro Subnetz sind 128 IP-Adressen und total sind es 1024.


| Subnetz ID | Netzwerk ID   | Verfügbare Adressen | Besetzte Adressen | Freie Adressen |
| ---------- | ------------- | ------------------- | ----------------- | -------------- |
| 1          | 37.105.96.0   | 125                 | 3                 | 123            |
| 2          | 37.105.96.129 | 125                 | 3                 | 123            |
| 3          | 37.105.97.0   | 125                 | 3                 | 123            |
| 4          | 37.105.97.129 | 125                 | 3                 | 123            |
| 5          | 37.105.98.0   | 125                 | 3                 | 123            |
| 6          | 37.105.98.129 | 125                 | 3                 | 123            |
| 7          | 37.105.99.0   | 125                 | 3                 | 123            |
| 4          | 37.105.99.129 | 125                 | 3                 | 123            |

Pro Subnetz ist eine IP-Adresse für den Router, für einen PC und für den anderen PC besetzt. 

### Excel Netzwerktabelle

Nach zwei Subnetzen ändert sich das dritte Oktett. Also beispielsweise von 37.105.**96**.1 auf 37.105.**97**.1.

<img width=50% height=50% alt="Netzwerk5und6" src="https://github.com/user-attachments/assets/ad1e491f-0a0b-4c9f-885d-3f1d55090071">

### PC Konfiguration

Ich habe bei jedem PC den **richtigen Gateway**, also die IP-Adresse vom **richtigen Interface** angegeben. Dann gab ich nur noch die IP-Adresse, die man aus der Namenskonvention auslesen konnte, ein und testete alles mit einem Ping zum anderen PC im gleichen Subnetz. 

<img width=50% height=50% alt="PCconfig-gateway" src="https://github.com/user-attachments/assets/db136e5e-e34e-410a-ab37-77b21400765f">

<img width=50% height=50% alt="PCconfig-ip" src="https://github.com/user-attachments/assets/ee59ec82-06c2-45f2-95c4-a2a355599115">

#### IP-Vergebung PCs

| ID  | Name    | IP-Adresse    | CIDR |
| --- | ------- | ------------- | ---- |
| 1   | PC-6002 | 37.105.96.2   | 25   |
| 2   | PC-6003 | 37.105.96.3   | 25   |
| 3   | PC-6130 | 37.105.96.130 | 25   |
| 4   | PC-6131 | 37.105.96.131 | 25   |
| 5   | PC-7002 | 37.105.97.2   | 25   |
| 6   | PC-7003 | 37.105.97.3   | 25   |
| 7   | PC-7130 | 37.105.97.130 | 25   |
| 8   | PC-7131 | 37.105.97.131 | 25   |
| 9   | PC-8002 | 37.105.98.2   | 25   |
| 10  | PC-8003 | 37.105.98.3   | 25   |
| 11  | PC-8130 | 37.105.98.130 | 25   |
| 12  | PC-8131 | 37.105.98.131 | 25   |
| 13  | PC-9002 | 37.105.99.2   | 25   |
| 14  | PC-9003 | 37.105.99.3   | 25   |
| 15  | PC-9130 | 37.105.99.130 | 25   |
| 16  | PC-9131 | 37.105.99.131 | 25   |

### Testing

Ich testete bei der Konfiguration den Ping zum anderen PC im selben Subnetz. Beispielsweise der Ping von PC-6002 zu PC-6003. Nachdem ich alles konfiguriert hatte testete ich die Kommunikation zwischen den Subnetzen. Das erste PDU wurde zum Router gesendet und wurde dann abgeworfen. Nachdem ich im Protokoll die Layers auslas, fiel mir auf, dass immer wenn ich das erste Mal ein Packet von einem Subnetz zu einem anderen sendete, es immer ein Layer 2 Problem war. Und zwar ist meine Vermutung, dass die ARP-Tabelle vom Router noch nicht ausgefüllt war und deswegen beim ersten Mal fehlschlägt. Erst beim zweiten Mal gelang das PDU an sein Ziel. 

<img width=50% height=50% alt="Testing-ping" src="https://github.com/user-attachments/assets/6d76eb9c-3e10-4dd6-b105-de24e07124e7">

<img width=50% height=50% alt="Testing-PDU" src="https://github.com/user-attachments/assets/ff0621cd-75e3-414f-9baa-f5b6fca24248">

### Fragen
- Wieviele freie IP-Adressen gibt es in der Abteilung **Marketing**?
- Eine neue Mitarbeiterin wird in der Abteilung **Marketing** eingestellt. Welche Netzwerkkonfiguration erhält sie?
- Ist das Netzwerk-Design sinnvoll?
- Gibt es Verbesserungsvorschläge bzgl. Netzwerk-Design?
- Welche zusätzlichen Informationen wären nützlich, um für dieses Netzwerk-Design einen Optimierungsvorschlag auszuarbeiten?

### Antworten
- In der Abteilung Marketing gibt es 123 freie IP-Adressen. 
- Sie erhält die IP-Adresse 37.105.97.132, den Gateway 37.105.97.129 und die Subnetzmaske 255.255.255.128. 
- Nicht wirklich. Es ist ein Netzwerk mit einem Single Point of Failure. Das heisst wenn der Router ausfällt gelangt keiner mehr ins Internet. 
- Wenn es einen Backup Router gäbe, wäre das Netzwerk gesichert. 
- Ob ein Internet Zugang gewünscht ist. 
