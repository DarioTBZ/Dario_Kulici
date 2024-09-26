
# Laufendem Windows Server ein EBS Volume hinzufügen

### Windows Server 2022 Instanz erstellen
Ich habe die Windows Server Instanz erstellt ohne die RDP Inbound Rule hinzuzufügen. Nach Aufgabe sollte das erst im Nachhinein gemacht werden. Als Key, habe ich meinen **Dario-1 Key** ausgewählt. 

### RDP Inbound Rule erstellen
Placeholder

Hier habe ich die RDP Inbound Rule erstellt, sodass *jede IP-Adresse* Zugriff auf diesen Port hat. So kann man sich später mit dem Microsoft Remote Desktop (andere Clients funktionieren auch) auf die Instanz einloggen. 

### Passwort anfordern
Placeholder

Um das Passwort anzufordern muss der **Private Key**, des Keypairs hochgeladen werden, damit AWS sicherstellen kann, dass nur die Person mit dem Key Zugriff auf den Server hat. Um sich per RDP verbinden zu können braucht es drei Informationen.

- IP Adresse oder Public DNS
- Benutzer
- Passwort

### Instanz Login
Placeholder

Da ich auf Mac arbeite, sieht das ein wenig anders aus als bei Windows. Das Passwort musste ich erst nach den Angaben des Public DNS und des Benutzers angeben, hat aber auf jeden Fall funktioniert. 

### Windows Drives anzeigen
Placeholder

Auf diesem Bild erkennt man nochmal, dass ich draufgekommen bin und nur der C Drive sichtbar ist. Hier soll dann später das zweite Volume erscheinen. 

### Availability Zone
Placeholder

Damit das Volume der Instanz hinzugefügt werden kann, muss es im gleichen Datenzentrum erstellt werden. Deswegen braucht man die Availability Zone. 

### Volume erstellen und anfügen
Placeholder

Hier sieht man, dass ich die richtige Availability Zone ausgewählt habe und musste nur noch die richtige Instanz auswählen. Wenn man auf das Drop Down Menu, geht sieht man noch die Instanzen Namen. 

### Ordner in neuem Volumen erstellen
Placeholder

Nachdem das Volume erstellt und angefügt wurde, erscheint es auch im Paritionsmanager auf dem Windowsserver. Dort musste ich es nur noch Online schalten, es aktivieren und partitionieren. Schon konnte ich den, im Auftrag erwähnten, Ordner erstellen. 

### Was passiert wenn man das Volume einfach detached?
Placeholder

Ich war mir sicher, dass das Volume auch entfernt werden konnte, wenn der Windows Server noch läuft. Trotzdem testete ich es aus, um 100% sicher zu sein. 

### Erkenntnis
Placeholder

Siehe da, das Volumen ist weg. Nicht nur im Explorer, sondern auch im Partitionsmanager. So wie erwartet. 