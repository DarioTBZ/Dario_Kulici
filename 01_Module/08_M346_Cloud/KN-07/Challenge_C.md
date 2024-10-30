# Webserver erstellen, Snapshot erstellen und neues Volume erzeugen

### IAM Rolle erstellen
Damit nicht jeder den Quellcode für die Webseite hat, schränkt man den Zugriff ein. Mit einer IAM Rolle kann man Instanzen erlauben auf dem S3 Bucket zuzugreifen. 

Placeholder01

Nach Aufgabe wählte ich S3ReadOnlyAccess aus. 

Placeholder02

Beim Erstellen der Rolle bekam ich **einen Fehler**. Anscheinend habe ich **nicht die Berechtigung, eine Rolle zu erstellen**. Das heisst ich schalte den Bucket auf **öffentlich**, was zwar unsicher ist aber damit ich den Auftrag abschliessen kann. 

Placeholder03

### S3 Bucket erstellen
Ich erstellte den S3 Bucket und setzte die Berechtigung für jeden frei. 

Placeholder04

Danach lade ich die Text Datei hoch und setze die Policy für jeden frei.

Placeholder05

### EC2 Webserver erstellen
Als nächstes ist der Webserver dran. Ich passte die User data ein wenig an. Mit `wget` wird die Datei vom Bucket heruntergeladen und die Ausgabe von `cat` wird in die index.html Datei geschrieben. 

Placeholder06

Auf diesem Bild sieht man den Webserver mit der IP 54.159.39.74. 

Placeholder07

### Snapshot erstellen
Um den Snapshot zu erstellen muss die Webserver Instanz ausgewählt werden. 

Placeholder08

### Image von Snapshot erstellen und Instanz deployen
Als letztes muss von diesem Snapshot ein Image erstellt werden, von dem dann die Instanz deployed wird. 

Placeholder09

Hier sieht man das erstellte Webserverimage von vorhin. 

Placeholder10

Nachdem die Instanz gestartet hat sieht man, dass die Seite geladen hat. 

Placeholder11

### Fazit
Die Nutzung von Snapshots ist sehr effizient. Man kann sie für Backups oder auch Images brauchen. 