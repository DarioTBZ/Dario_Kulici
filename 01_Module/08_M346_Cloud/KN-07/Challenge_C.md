# Webserver erstellen, Snapshot erstellen und neues Volume erzeugen

### IAM Rolle erstellen
Damit nicht jeder den Quellcode für die Webseite hat, schränkt man den Zugriff ein. Mit einer IAM Rolle kann man Instanzen erlauben auf dem S3 Bucket zuzugreifen. 

<img width=50% height=50% alt="Placeholder01" src="https://github.com/user-attachments/assets/d69d354c-9d1e-4db5-af05-3930bfb9ea84">

Nach Aufgabe wählte ich S3ReadOnlyAccess aus. ![Placeholder11](https://github.com/user-attachments/assets/e73607f8-1070-43a4-b29c-9433c77d607d)


<img width=50% height=50% alt="Placeholder02" src="https://github.com/user-attachments/assets/76b41d61-1b2e-4814-9d7c-1570c4d0c56d">

Beim Erstellen der Rolle bekam ich **einen Fehler**. Anscheinend habe ich **nicht die Berechtigung, eine Rolle zu erstellen**. Das heisst ich schalte den Bucket auf **öffentlich**, was zwar unsicher ist aber damit ich den Auftrag abschliessen kann. 

<img width=50% height=50% alt="Placeholder03" src="https://github.com/user-attachments/assets/1ab63e24-2030-4d93-983f-0e6a74c3e8f6">

### S3 Bucket erstellen
Ich erstellte den S3 Bucket und setzte die Berechtigung für jeden frei. 

<img width=50% height=50% alt="Placeholder04" src="https://github.com/user-attachments/assets/97c4d299-3295-49cb-b05b-28944c0f3470">

Danach lade ich die Text Datei hoch und setze die Policy für jeden frei.

<img width=50% height=50% alt="Placeholder05" src="https://github.com/user-attachments/assets/f375a533-e80d-48ed-b839-f4452a980c35">

### EC2 Webserver erstellen
Als nächstes ist der Webserver dran. Ich passte die User data ein wenig an. Mit `wget` wird die Datei vom Bucket heruntergeladen und die Ausgabe von `cat` wird in die index.html Datei geschrieben. 

<img width=50% height=50% alt="Placeholder06" src="https://github.com/user-attachments/assets/9779ebd2-9b99-42d2-b398-129ecb515344">

Auf diesem Bild sieht man den Webserver mit der IP 54.159.39.74. 

<img width=50% height=50% alt="Placeholder07" src="https://github.com/user-attachments/assets/d9043907-dff5-4e52-a49c-be432a15cb0c">

### Snapshot erstellen
Um den Snapshot zu erstellen muss die Webserver Instanz ausgewählt werden. 

<img width=50% height=50% alt="Placeholder08" src="https://github.com/user-attachments/assets/fea9a120-7dd0-414c-9f34-2823275c5c68">

### Image von Snapshot erstellen und Instanz deployen
Als letztes muss von diesem Snapshot ein Image erstellt werden, von dem dann die Instanz deployed wird. 

<img width=50% height=50% alt="Placeholder09" src="https://github.com/user-attachments/assets/dc53ea3e-fa4a-4541-ba99-4e6d973123c2">

Hier sieht man das erstellte Webserverimage von vorhin. 

<img width=50% height=50% alt="Placeholder10" src="https://github.com/user-attachments/assets/ed07ca90-35fc-4d5d-9597-0a020f20a6c6">

Nachdem die Instanz gestartet hat sieht man, dass die Seite geladen hat. 

<img width=50% height=50% alt="Placeholder11" src="https://github.com/user-attachments/assets/0c667978-af19-4bd5-8d80-3d42344094a5">

### Fazit
Die Nutzung von Snapshots ist sehr effizient. Man kann sie für Backups oder auch Images brauchen. 
