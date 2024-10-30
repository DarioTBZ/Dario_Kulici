# Auto Scaler und Load Balancer kombinieren

### Aktuelle Lage
Jetzt habe ich einen Load Balancer alleine und einen Auto Scaler alleine erstellt. Einzeln sind diese Services nicht sehr effektiv. Aber sobald sie zusammen fungieren, könnte man dieses Konzept bei Firmen als professionelle Lösung deployen. In dieser Challenge kombiniere ich diese beiden Services. 

### Target Group erstellen
In der Target Group werden Instanzen erfasst, auf die der traffic verteilt werden muss. Als erstes definiert man, dass man den traffic auf Instanzen verteilen will. 

Placeholder01

Auf diesem Bild müssen die Instanzen ausgewählt werden. Hier wählte ich, die vom Auto Scaler erstellte Instanzen. 

Placeholder02

### Load Balancer erstellen
Der Load Balancer wird den traffic auf verschiedene Instanzen verteilen, die in der Target Group definiert sind. Ich erstelle den Application Load Balancer und passe die Einstellungen an. Das Wichtigste dabei ist, dass er im gleichen VPC wie die Instanzen ist. Somit können sie kommunizieren und es enstehen keine Fehler. 

Placeholder 03

Anbei sieht man, dass die vorher erstellte Target Group ausgewählt werden muss. 

Placeholder04

In der Summary sind alle Einstellungen zusammengefasst. Der Load Balancer KN06-KUL-ALB1 wird im M346-KUL-VPC mit der Security Group K346-KUL-Web-Access erstellt und verteilt den traffic auf Port 80 der Instanzen. 

Placeholder05

Zum Schluss muss der Load Balancer nur noch unter der Auto Scaling Group ausgewählt werden. 

Placeholder06

### Fazit
Alles in allem hat es sauber funktioniert und ich hatte keine Schwierigkeiten bei der Aufgabe. Da ich momentan nur einen Laptop zur Verfügung habe, kann ich nicht beweisen, dass der Load Balancer funktioniert und den traffic tatsächlich verteilt. Ich kann nur ein Bild aufzeigen, wo er aktiv ist. 

Placeholder07