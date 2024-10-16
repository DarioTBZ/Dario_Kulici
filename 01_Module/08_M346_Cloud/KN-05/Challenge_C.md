# Zwei Instanzen innerhalb der erstellten VPC deployen

### Security Groups
Als erstes erstellte ich die Security Groups. Hier ist eine Übersicht mit den Inbound Regeln. Die Outbound Regel ist offen, weshalb sie nicht in der Tabelle ersichtlich ist. 

##### Web Server Security Group

###### M346-KUL-Web-Access

| Protokoll | Port | Zugang von | Beschreibung                                                                                                                                     |
| --------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| HTTP      | 80   | 0.0.0.0/0  | Jeder sollte auf die Webseite zugreifen können, weshalb der Zugang so konfiguriert ist.                                                          |
| SSH       | 22   | 0.0.0.0/0  | Theoretisch darf nicht jeder per SSH auf den Webserver zugreifen. Da der Zugriff aber mit einem Key geregelt ist, kann der Port geöffnet werden. |

##### Private Instance Security Group

###### M346-KUL-Priv-Only

| Protokoll | Port | Zugang von         | Beschreibung                                                                        |
| --------- | ---- | ------------------ | ----------------------------------------------------------------------------------- |
| ICMP      | -    | M346-KUL-Priv-Only | Nur die Instanzen, die die diese Security Group haben, können diese Instanz pingen. |

Das Ping Protokoll heisst ICMP (Internet Control Message Protocol). Damit diese Instanz per Ping erreicht werden kann muss das in der Security Group erfasst werden. Der Webserver hat die Security Group M346-KUL-Web-Access. Somit muss in dieser Security Group erlaubt werden, dass die *Security Group vom Webserver per ICMP Zugang auf die Instanz* hat. 

### Redundanz / Hochverfügbarkeit

##### Situation
Die momentane Konfiguration ist *weder Redundant noch immer Verfügbar*. Das liegt daran, dass pro AZ zwei Netze (public und private) vorhanden sind und der Webserver auf einer AZ basiert ist. Wenn diese AZ ausfällt ist der **komplette Webserver offline**. Die Daten vom Webserver sind nur 1-fach gesichert. Wenn Hacker die Daten stehlen gibt es **kein Backup** oder ähnliches, wo die Daten noch wiederhergestellt werden könnten. 

##### Lösung
Die optimale Lösung wäre, den Webserver auf **mehrere Instanzen** in verschiedenen AZ aufzuteilen. So würde der **Webservice nicht ausfallen**, falls eine Instanz einen Fehler oder ein Problem hat. Ausserdem sollte man *pro AZ einen Gateway* haben, denn wenn die AZ mit dem Gateway offline ist, verlieren alle Instanzen in den private subnets die Internetverbindung. 

### Beweis Webseite
Placeholder01

Auf dem Bild erkennt man den funktionierenden Webserver und die öffentliche IP Adresse (3.238.77.83). 

### SSH Zugriff Webserver
Placeholder02

Hier sieht man, dass der SSH Zugriff ebenfalls erfolgreich ist (ping 10.0.4.46). Die private IP Adresse habe ich von den Instanzdetails auf AWS entnommen. 

### Erfolgreicher Ping
Placeholder03

Der Ping vom Webserver auf die Instanz im privaten Subnetz gelingt mir. 