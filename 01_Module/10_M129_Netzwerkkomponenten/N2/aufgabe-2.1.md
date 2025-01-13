# N1 Aufgabenstellung 2.1

### Vorgaben
- IP Range vom ISP: 133.96.48.0/23
- Vier gleichgrosse Subnetze


### Netzwerk
Der ISP stellt ein /23er Netz zur Verfügung und für den Auftrag wird das in ein **/25er Netz** aufgeteilt. Pro Subnetz sind 128 IP-Adressen zur Verfügung und total sind es 512.  

| Subnetz ID | Netzwerk ID   | Verfügbare Adressen | Besetzte Adressen | Freie Adressen |
| ---------- | ------------- | ------------------- | ----------------- | -------------- |
| 1          | 133.95.48.0   | 126                 | 3                 | 123            |
| 2          | 133.95.48.128 | 126                 | 3                 | 123            |
| 3          | 133.95.49.0   | 126                 | 3                 | 123            |
| 4          | 133.95.49.128 | 126                 | 3                 | 123            |

Pro Subnetz ist eine IP für den Router und zwei für PCs. 

#### Excel Netzwerktabelle

Die ersten zwei Subnetze sind ganz normal also bspw. 133.95.48.0. Beim dritten Netzwerk wird noch ein Bit auf True geschalten und somit ist die IP-Adresse 133.95.**49**.0. So bringt man 512 IP-Adresse in vier Subnetze. 

<img width=50% height=50% alt="Netzwerk3" src="https://github.com/user-attachments/assets/83406787-6319-4450-8afb-2b5a8a371476">



<img width=50% height=50% alt="Netzwerk4" src="https://github.com/user-attachments/assets/2c074b9d-46ae-41e2-93eb-d6c78273bf27">

#### IP-Vergebung PCs

| ID  | Name    | IP-Adresse   | CIDR |
| --- | ------- | ------------ | ---- |
| 1   | PC-8050 | 133.95.48.50 | 25   |
| 2   | PC-8080 | 133.95.48.80 | 25   |
| 3   | PC-8130 | 133.95.48.30 | 25   |
| 4   | PC-8140 | 133.95.48.40 | 25   |
| 5   | PC-9050 | 133.95.49.50 | 25   |
| 6   | PC-9080 | 133.95.49.80 | 25   |
| 7   | PC-9130 | 133.95.49.30 | 25   |
| 8   | PC-9140 | 133.95.49.40 | 25   |


### PCs

Ich habe die PCs sauber konfiguriert, sodass sie die IP-Adresse im Namen nehmen konnten. 

<img width=50% height=50% alt="PCconfig" src="https://github.com/user-attachments/assets/5daab414-d07a-4c28-8c7e-549d04508bac">

Hier ist ein Beispiel mit PC-8050 also der IP-Adresse 133.95.48.**50**. 

<img width=50% height=50% alt="PCconfig2" src="https://github.com/user-attachments/assets/20240b69-7c17-4e49-9bae-5139a7f6a85a">

Bei den PCs musste ich nur die **IP-Adresse, Subnetzmaske und den Gateway** bestimmen. 

### Testing
Zum testen des Netzwerks erstelle ich ein PDU, dass von PC-8050 zu PC-9140 gehen sollte. 

<img width=50% height=50% alt="Testing1" src="https://github.com/user-attachments/assets/8c317315-ed9f-40ce-9df8-9de55aa233a9">

<img width=50% height=50% alt="Testing2" src="https://github.com/user-attachments/assets/859b6b28-2c24-4d9e-bf19-a2642ac8e0e6">

<img width=50% height=50% alt="Testing3" src="https://github.com/user-attachments/assets/adf33cfb-25d9-4c67-9592-96066c8d6aff">

Man sieht, dass das Paket erfolgreich das Ziel erreicht und dann zurück versendet wird. Somit gelang mir dieser Auftrag. 

### Fragen 
- Wie viele freie IP-Adressen gibt es in der Abteilung **Einkauf**
- Ist ein mögliches Wachstum der Firma berücksichtigt?
- Ist das Netzwerk-Design sinnvoll?
- Gibt es Verbesserungsvorschläge bzgl. Netzwerk-Design?
- Welche zusätzlichen Informationen wären nützlich, um für dieses Netzwerk-Design einen Optimierungsvorschlag auszuarbeiten?

### Antworten
- In der Abteilung Einkauf gibt es 123 freie IP-Adressen
- Ja ist es, denn es sind genügend IP-Adressen verfügbar. 
- Ja ist es. Verschiedene Subnetze für Abteilungen zu haben ist übersichtlich. 
- Momentan gibt es einen Single Point of Failure und zwar der Router. Man könnte einen Backup Router mit einem anderen Anbieter an das Netzwerk schliessen. 
- Wie viele Mitarbeiter pro Jahr etwa dazukommen. 
