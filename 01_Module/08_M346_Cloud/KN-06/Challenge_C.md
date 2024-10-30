# Auto-Scaling Group erstellen

### Launch Template

Als erstes erstellte ich das Launch Template. Dieses dient dazu, dass wenn Instanzen erstellt werden sollen, sie nach dieser Vorlage erstellt werden. Somit kann man klar definieren, was für Instanzen man deployen möchte. 

Unter advanced fügte ich diesen Code ein. 
```
#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
EC2AZ=$(TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` && curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/placement/availability-zone)
echo '<center><h1 style="background-color:powderblue;">M346 KN06 C - Diese EC2 Instanz ist in der AZ: AZID </h1></center>' > /var/www/html/index.txt
sed "s/AZID/$EC2AZ/" /var/www/html/index.txt > /var/www/html/index.html
```

Dieser Code aktualisiert die Instanz mit den neusten Paketen, lädt das Paket httpd herunter, startet den httpd Service und lässt ihn beim Start automatisch starten. Dann wird eine Variable EC2AZ definiert, die ein Token erstellt. Danach wird HTML Code geschrieben, der anzeigen soll, in welcher Availability Zone die Instanz ist. AZID wird am Schluss durch die erhaltene Availability Zone ersetzt. 

### Auto Scaling Group
Der zweite Schritt ist, die Autoscaling Group zu erstellen und das Launch Template auswählen. Auf dem Bild sieht man, das ausgewählte Launch Template. 

<img width=50% height=50% alt="Placeholder01" src="https://github.com/user-attachments/assets/69f79e69-5c12-412f-b14a-872bccf7682b">

Hier überprüfe ich kurz, ob die Instanzen in verschiedenen Availability Zones sind. 

<img width=50% height=50% alt="Placeholder02" src="https://github.com/user-attachments/assets/3d908079-88b1-4452-babf-06fecd2239e1">

Auf dem Bild sieht man, dass sie in den Availability Zones 1a und 1b sind. Anbei noch der Beweis, dass der Code funktioniert hat. 

<img width=50% height=50% alt="Placeholder03" src="https://github.com/user-attachments/assets/fbdaaa00-8ff1-4ff0-9633-4a75803ff3a9">

### Fazit
Ich habe die Auto Scaling Group erstellt, ein Launch Template erstellt und ausgewählt und die Namen korrekt gesetzt. 

Der Auto Scaler erstellt je nach Einstellung neue Instanzen und löscht diese wieder. Der Unterschied zu einem Load Balancer ist, dass der Load Balancer den **traffic** auf Instanzen verteilt und ein Auto Scaler **Instanzen erstellt**. In Kombination sind diese Services sehr effizient und werden sicher bei den meisten Firmen so benutzt. 

High Availability bedeutet hohe Verfügbarkeit. Eine Firma hat beispielsweise ein Produkt, das sie bereitstellt. Es ist eine App, die etwas kann. Diese App muss gehostet werden, damit Nutzer auf sie zugreifen können. Das Ziel ist es, die **App 24/7 online** zu haben, damit Nutzer für sie **bezahlen**. Wenn die App offline ist oder crashed bezahlen die Nutzer nicht, weil sie nicht wissen ob sie immer verfügbar ist. Deswegen ist eine High Availability nötig, um zu vermeiden, dass das die App keine Einnahmen bringt. 