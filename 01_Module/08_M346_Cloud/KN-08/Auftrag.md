# Auftrag KN-08

## Einleitung

Der Auftrag in KN-08 ist keine Anleitung, die man befolgt und dann dokumentiert, sondern ein Auftrag einen **eigenen Auftrag zu erstellen**. Also das, in diesem Modul, Gelernte **praktisch umzusetzen**. In dieser Dokumentation werde ich genau zeigen *was ich gemacht hatte, wie ich es gemacht hatte und was für Schwierigkeiten und Probleme dabei auftauchten.* 

### Idee

Ich interessiere mich nicht nur für Plattformentwickler-spezifische Themen, sondern auch für Applikationsentwickler-Themen wie beispielsweise programmieren. Nicht all zu lange habe ich ein **Server-Client-Modell** mit Python programmiert. Es ist ein Chatroom-Server an dem sich Clients verbinden und mit **anderen Clients kommunizieren** können. Da der Schulstress zunahm konnte ich nicht viel daran weiterarbeiten. Jetzt hat es aber einen Zweck. Die Idee ist es, das **Server-Client-Modell in der AWS Cloud umzusetzen**. 

Um das Modell in der Cloud zu deployen muss es aber ein *wenig angepasst werden*. Momentan gibt es nur **einen** Server, der Anfragen verarbeiten kann. Was wenn es **mehrere** Server geben könnte. Somit könnte ein Auto-Scaler erstellt werden, der *mehrere Instanzen erstellt* und den Server darauf startet. Der traffic würde durch einen **Load Balancer** gleichmässig auf die Instanzen verteilt werden. Falls eine maximale Menge an Clients für einen Server erreicht wäre, würden einfach **noch mehr Server erstellt** werden. 

Diese Idee ist nicht zu einfach aber nicht zu schwierig für die Umsetzung und ist meiner Meinung nach perfekt für dieses Modul. 

## Vorbereitung

Der Hauptteil der Vorbereitung ist die **Programmierung vom Server**. Der Server muss so programmiert sein, dass *mehrere Server miteinander kommunizieren und Anfragen verarbeiten* können. Jeder Server muss von Clients erhaltene Nachrichten an **alle Server broadcasten**, damit jeder **Client die Nachricht sehen** kann, *egal auf welchem Server* er verbunden ist. 

### Serverkonzept

Es gibt einen zentralen Master Server. Dieser ist dient als Load Balancer. Clients verbinden sich auf seine Public IP und werden einem Chatroom Server zugewiesen. Egal auf welchen Server ein Client ist, er bekommt die Nachricht. Nach diesem Konzept passte ich den Python Code an, den ich hatte. 

### Cloud-Init und S3 Bucket

Das Server Script muss von den Instanzen heruntergeladen werden. Für das habe ich eine Cloud-Init Datei erstellt, die alles für den Server bereitstellt. Das Server Script wird von einem S3 Bucket mithilfe von `wget` geholt. 

## Umsetzung in der Cloud

### S3 Bucket

Ich erstellte einen S3 Bucket und legte alle benötigten Dateien darin ab. Dabei musste ich die Permissions anpassen, sodass der Bucket öffentlich zugänglich wurde. 

Placeholder05

### Master Server

Als erstes erstellte ich den Master Server. Dieser dient als zentrale Verwaltung von den Instanzen. Dabei war sehr wichtig, dass dieses eine Public IP hat und das Master Server Script vom S3 Bucket herunterlädt. Hier habe ich die Cloud-Init Datei vom Master Server eingefügt.

```
#cloud-config

runcmd:
  - wget -O /home/ubuntu/master_server.py https://kn-08-bucket.s3.us-east-1.amazonaws.com/master-server_v1.py
  - chmod +x /home/ubuntu/master_server.py
  - nohup python3 /home/ubuntu/master_server.py > /home/ubuntu/master_server.log 2>&1 &
```

Er holt zuerst das Script vom S3 Bucket und lädt es in die Datei `master_server.py`. Nachher gibt er mit `chmod +x` Ausführ-Rechte, damit die Datei ausgeführt werden kann und führt sie im Hintergrund aus. Das coole ist, dass der Output live in die Datei `master_server.log` geschrieben wird und man diesen mit `tail -f master_server.log` mitverfolgen kann. Ich musste sehr oft per SSH auf die Instanz, um zu prüfen warum etwas nicht funktionierte. So war es sehr effizient und angenehm. 

Nach einigen Versuchen und gelöschten Instanzen funktionierte der Master Server wie er sollte. Somit konnte ich fortfahren. 

### Chatroom Server

Chatroom Server werden vom Master Server verwaltet. Die Idee war es den Auto-Scaler von AWS zu nutzen. Leider ging mir die Zeit aus und es passierten zu viele Script Fehler, sodass die Sache unstabil war. Deswegen habe ich manuell (also immer noch mit Cloud-Init) zwei Chatroom Server erstellt. Hier die Cloud-Init davon.

```
#cloud-config

packages:

- redis

- python3-redis

- python3-requests

  

runcmd:

- sudo sed -i "s/^bind .*/bind 0.0.0.0/" /etc/redis/redis.conf

- sudo sed -i "s/^protected-mode yes/protected-mode no/" /etc/redis/redis.conf

- sudo systemctl restart redis

- wget -O /home/ubuntu/chatroom_server.py https://s3.amazonaws.com/BUCKET_NAME/FILE_NAME

- chmod +x /home/ubuntu/chatroom_server.py

- nohup python3 /home/ubuntu/chatroom_server.py > /home/ubuntu/chatroom_server.log 2>&1 &

```

Diese ist etwas komplexer. Zusammengefasst werden notwendige Pakete für den Serverbetrieb heruntergeladen und eingerichtet. Beispielsweise brauchte ich `redis` um den traffic zwischen den zwei Servern zu verteilen. Der Server wird hierbei mit dem gleichen Hintergrundprinzip vom Master Server gestartet. 

### Fehlgeschlagener Versuch

Um sicherzustellen, dass das Konzept funktioniert habe ich sehr sehr viel getestet. Anbei schaffte ich es zwei Clients auf zwei verschiedene Chatroom Server zu verbinden, aber die Nachrichten sah man leider nicht auf beiden Clients. Auf den Bildern sieht man die IPs von den Instanzen auf den Clients und auf AWS. 

Placeholder03
Placeholder04

Das Problem war hauptsächlich, dass die Chatroom Server die Nachrichten von den Clients nie an andere Server sendete, weshalb die Clients nicht miteinander kommunizieren konnten. 

### Finaler Erfolg

Schlussendlich schaffte ich es endlich das Konzept umzusetzen. Zwar hatte ich keinen Load Balancer oder Auto Scaling Group, aber dafür ganz viel Erfahrung mit AWS + Python. Auf den Bildern erkennt man den erfolgreichen Versuch, bei dem sich zwei Clients an den Master Server verbinden und miteinander kommunizieren können. 

Placeholder08
Placeholder06

## Fazit

Ich finde dieses Modul hat sehr viel Spass gemacht und ich habe viel gelernt. Danke an Herr Callisto für die Motivation und Energie, die sie mitgegeben haben! Leider konnte ich mein Konzept nicht so ausführen wie ich es mochte, aber ich habe das Beste daraus gemacht. 