# Snapshot von EBS Volume erstellen und wieder restoren

### EBS Volume erstellen
Ich erstelle das EBS Volume und attache es der Lab Instanz. 

<img width=50% height=50% alt="Placeholder01" src="https://github.com/user-attachments/assets/7e621a62-b475-4cfb-824c-dcdc41bdb37d">

Wenn man `df` eingibt, also die Dateisystemes ausgibt ist das zugewiesene Volume noch nicht zu sehen. Also erstelle ich das Filesystem. 

<img width=50% height=50% alt="Placeholder02" src="https://github.com/user-attachments/assets/f5d91bad-d699-4014-9b9d-d91da29838d8">

Danach erstelle ich einen Ordner im Mount Ordner und mounte das erstellte Filesystem. Auf dem Bild sieht man, das erschienene `dev/xvdf`, das auf data-store gemounted wurde. 

Placeholder03<img width=50% height=50% alt="Placeholder03" src="https://github.com/user-attachments/assets/8177b778-ba75-4420-af40-d17032cd2e61">

Als nächstes erstelle ich eine Datei mit Inhalt, die dann gesichert wird. 

Placeholder04<img width=50% height=50% alt="Placeholder04" src="https://github.com/user-attachments/assets/94e4effb-82f0-4f82-8052-f47baa60fde6">

Hier erstelle ich einen Snapshot des Volumes. 

<img width=50% height=50% alt="Placeholder05" src="https://github.com/user-attachments/assets/b3c8b88b-2bcf-470c-91c8-9f5158d738b1">

Zum testen lösche ich die Datei auf der Instanz. 

<img width=50% height=50% alt="Placeholder06" src="https://github.com/user-attachments/assets/3723a229-c32f-4c20-91ea-a6c9afa19a4e">

### Restore vom Snapshot

Von diesem Snapshot erstelle ich ein Volume, welches dann auf die Instanz gemounted wird. 

<img width=50% height=50% alt="Placeholder07" src="https://github.com/user-attachments/assets/783706d2-76e1-4dec-9dee-65c2bdc9e1a3">

Das mounte ich und siehe da die Datei ist noch vorhanden. 

<img width=50% height=50% alt="Placeholder08" src="https://github.com/user-attachments/assets/14e68699-df3a-42d1-b086-7b6a8b9d693f">

### Fazit
Snapshots sind eine effiziente Möglichkeit Volumen zu sichern. Bei einem Ausfall oder Fehler kann man jederzeit den letzten Snapshot restoren. 
