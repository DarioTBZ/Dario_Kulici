
# Laufendem Windows Server ein EBS Volume hinzufügen

### Windows Server 2022 Instanz erstellen
Ich habe die Windows Server Instanz erstellt ohne die RDP Inbound Rule hinzuzufügen. Nach Aufgabe sollte das erst im Nachhinein gemacht werden. Als Key, habe ich meinen **Dario-1 Key** ausgewählt. 

### RDP Inbound Rule erstellen
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/e225d372-f055-4897-9b9a-3debfe0f81d4">

Hier habe ich die RDP Inbound Rule erstellt, sodass *jede IP-Adresse* Zugriff auf diesen Port hat. So kann man sich später mit dem Microsoft Remote Desktop (andere Clients funktionieren auch) auf die Instanz einloggen. 

### Passwort anfordern
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/5b953e87-06c6-4dbe-9fc8-46f2cd9009f1">

Um das Passwort anzufordern muss der **Private Key**, des Keypairs hochgeladen werden, damit AWS sicherstellen kann, dass nur die Person mit dem Key Zugriff auf den Server hat. Um sich per RDP verbinden zu können braucht es drei Informationen.

- IP Adresse oder Public DNS
- Benutzer
- Passwort

### Instanz Login
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/651c0a33-7f19-4ea2-80db-43492dee5064">

Da ich auf Mac arbeite, sieht das ein wenig anders aus als bei Windows. Das Passwort musste ich erst nach den Angaben des Public DNS und des Benutzers angeben, hat aber auf jeden Fall funktioniert. 

### Windows Drives anzeigen
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/f6e3b9fd-a7a0-44e5-bae3-eb86fcdac52d">

Auf diesem Bild erkennt man nochmal, dass ich draufgekommen bin und nur der C Drive sichtbar ist. Hier soll dann später das zweite Volume erscheinen. 

### Availability Zone
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/1740de1d-7520-4e16-82b9-c805d5dd8779">

Damit das Volume der Instanz hinzugefügt werden kann, muss es im gleichen Datenzentrum erstellt werden. Deswegen braucht man die Availability Zone. 

### Volume erstellen und anfügen
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/6b4b61a6-c0d3-497b-b79d-3e261d8299af">

Hier sieht man, dass ich die richtige Availability Zone ausgewählt habe und musste nur noch die richtige Instanz auswählen. Wenn man auf das Drop Down Menu, geht sieht man noch die Instanzen Namen. 

### Ordner in neuem Volumen erstellen
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/6c53f0d0-fadc-4c0c-8391-d81a0ee09679">

Nachdem das Volume erstellt und angefügt wurde, erscheint es auch im Paritionsmanager auf dem Windowsserver. Dort musste ich es nur noch Online schalten, es aktivieren und partitionieren. Schon konnte ich den, im Auftrag erwähnten, Ordner erstellen. 

### Was passiert wenn man das Volume einfach detached?
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/3da6d9f4-14fa-4681-a336-8510d53dbae5">

Ich war mir sicher, dass das Volume auch entfernt werden konnte, wenn der Windows Server noch läuft. Trotzdem testete ich es aus, um 100% sicher zu sein. 

### Erkenntnis
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/f4764c63-94dc-4cd1-b729-cd0822e1c075">

Siehe da, das Volumen ist weg. Nicht nur im Explorer, sondern auch im Partitionsmanager. So wie erwartet. 
