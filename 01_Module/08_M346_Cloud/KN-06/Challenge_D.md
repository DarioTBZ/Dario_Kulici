# Auto Scaler und Load Balancer kombinieren

### Aktuelle Lage
Jetzt habe ich einen Load Balancer alleine und einen Auto Scaler alleine erstellt. Einzeln sind diese Services nicht sehr effektiv. Aber sobald sie zusammen fungieren, könnte man dieses Konzept bei Firmen als professionelle Lösung deployen. In dieser Challenge kombiniere ich diese beiden Services. 

### Target Group erstellen
In der Target Group werden Instanzen erfasst, auf die der traffic verteilt werden muss. Als erstes definiert man, dass man den traffic auf Instanzen verteilen will. 

<img width=50% height=50% alt="Placeholder01" src="https://github.com/user-attachments/assets/72a3fc88-e041-454b-9732-19e18ef6020e">

Auf diesem Bild müssen die Instanzen ausgewählt werden. Hier wählte ich, die vom Auto Scaler erstellte Instanzen. 

<img width=50% height=50% alt="Placeholder02" src="https://github.com/user-attachments/assets/55350fc9-5375-4ce1-8273-62d692aa76a7">

### Load Balancer erstellen
Der Load Balancer wird den traffic auf verschiedene Instanzen verteilen, die in der Target Group definiert sind. Ich erstelle den Application Load Balancer und passe die Einstellungen an. Das Wichtigste dabei ist, dass er im gleichen VPC wie die Instanzen ist. Somit können sie kommunizieren und es enstehen keine Fehler. 

<img width=50% height=50% alt="Placeholder03" src="https://github.com/user-attachments/assets/5ac8c93f-ce4b-4729-99b8-659734531fca">

Anbei sieht man, dass die vorher erstellte Target Group ausgewählt werden muss. 

<img width=50% height=50% alt="Placeholder04" src="https://github.com/user-attachments/assets/e964ddcb-900e-41fa-a43f-e878a2682749">

In der Summary sind alle Einstellungen zusammengefasst. Der Load Balancer KN06-KUL-ALB1 wird im M346-KUL-VPC mit der Security Group K346-KUL-Web-Access erstellt und verteilt den traffic auf Port 80 der Instanzen. 

<img width=50% height=50% alt="Placeholder05" src="https://github.com/user-attachments/assets/7695d56b-9d37-48f6-b2d0-cc0a45218783">

Zum Schluss muss der Load Balancer nur noch unter der Auto Scaling Group ausgewählt werden. 

<img width=50% height=50% alt="Placeholder06" src="https://github.com/user-attachments/assets/74e9ef73-62fb-41cc-b51a-023c0a7ace18">

### Fazit
Alles in allem hat es sauber funktioniert und ich hatte keine Schwierigkeiten bei der Aufgabe. Der Load Balancer funktioniert gut. Anbei ein Beweisvideo. 

