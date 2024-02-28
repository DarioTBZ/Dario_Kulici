# Aufgabe 1: Der Konfigurationsfehler
Nach der erfolgreichen Installation des Projekts habe ich mich an die **Konfiguration** gesetzt. Den alten Router löschen, den neuen importieren und verbinden. Mit dem Kabel Symbol an der linken Seite kann man Verknüpfungen machen. 
![](Bild%201.png)

Der Ping war auch **erfolgreich**, wie man im Bild unten erkennen kann. Alle Pakete, die gesendet wurden, wurden auch empfangen. 

Welche Services müssen aktiv sein, wenn der Ping erfolgreich ist?

**DNS und DHCP**, weil *tbz.ch* eine Domain ist braucht es einen *DNS Server*, der die Anfrage beantwortet und DHCP, um *überhaupt* ins Internet zu gelangen. 
![](Bild%202.png)

# Aufgabe 2: HTTP Traffic beobachten und aufzeichnen
Zuerst musste ich alle Geräte starten. Dann öffnete ich Wireshark, um den Traffic mitzulesen. Im Bild erkennt man den **GET Befehl**. In der unteren Leiste sieht man auch den Destination Port (80). *HTTP* ist auf **Port 80**. 
![](Bild%203.png)
![](Bild%204.png)

## Fragen beantworten

Der User Agent bzw. der Browser vom Client ist Firefox. Hier ist der Beweis: 
![](Bild%205.png)

Um zu sehen wie viele Dateien heruntergeladen wurde muss einfach überprüft werden *wie viele GET Befehle* ausgeführt wurden und ob Dateien unter "Info" stehen. Das "/" sagt aus wo sich die Datei befindet. Insgesamt sind es **12 Dateien**. 
![](Bild%208.png)

Der Server benutzt gzip als Encoder. 
![](Bild%207.png)


Der Server hat die Version 2.4.56. 
![](Bild%206.png)

# Aufgabe 3: Webserver Erstinspektion

### Uname - Informationen über das System auslesen
| Unix Betriebssystem | Linux Kernel | Kernelversion aktuell? | Prozessorarchitektur | Hinweise auf Distribution |
| ------------ | ------------ | ---------------------- | -------------------- | ------------------------- |
| Linux (Debian 11 Bullseye)             | 5.10.0-23-cloud-amd64             | Nein                       | 64 Bit                     | Ja                          |
- Der Linux Kernel ist veraltet. Die neuste Version für Debian 11 ist 6.1.0-9. Mit Debian 12 könnte man sogar 6.3.0-2 auf den Webserver laden. 

### cat /etc/issue
Mit dem `cat` Befehl wird die laufende Linux Distribution ausgelesen. Allerdings sieht man diese schon mit dem `Uname` Befehl. Die laufende Linux Distribution ist Debian. 

### IP Konfiguration
| ens4          | lo  |
| ------------- | --- |
| 192.168.29.10/24 | 127.0.0.1/8    |

ens4 ist der Ethernet Adapter. "Lo" steht für Loopback und ist ein virtuelles interface. Standartmässig nutzt das Loopback interface die IP Range 127.0.0.0/8 (255.0.0.0) um mit sich selbst zu kommunizieren. Falls keine Netzwerkadapter vorhanden sind, kann der PC nicht mehr kommunizieren. Mit dem Loopback sind Systemanalysen möglich. Beispielsweise kann man prüfen, ob das TCP funktioniert, indem man die Loopback Adresse pingt. 

### Netstat - Network Statistics
Die Ports 22 und 80 sind offen. Port 22 ist SSH, damit per SSH auf das System zugegriffen werden kann und Ports 80 ist HTTP, das Webprotokoll. Wenn ein Client auf die Webseite des Webservers zugreifen will, geht er über Port 80, um die Webseite anzufordern. Falls sich jemand von einem anderen Client mit dem Webserver verbinden will, kann das über SSH (über Port 22) gemacht werden. 

HTTP (Hyper Text Transfer Protocol): Übertragungsprotokoll, überträgt Daten der Webseite zu Clients.
SSH (Secure Shell): Remote Zugriff auf Geräte im Internet.

###  Disk Space Usage
Die Hauptdisk ist 1.9 GB gross, 1.1 GB davon sind in Benutzung. Frei sind also 0.8 GB. Es ist sicher genügend Speicherplatz für einen Webserver solange der Speicher nicht voll ist. Das System ist in 2 Partitionen unterteilt: `/dev/sda1` und `/dev/sda15`. 

### Leistungsanalyse
Der `systemd` Dienst benötigt etwa Sekunden CPU Zeit. Insgesamt sind 498 MB RAM verbaut. 50 MB werden davon gebraucht. Es ist also genügend RAM vorhanden. 
**Wichtig**: MiB und MB sind nicht das gleiche! 1024 Bytes (2¹⁰) sind 1 Kilobyte. Im Dezimalsystem steht Kilo für 1000. Demnach müsste ein Kilobyte aus 1000 Byte (10³)  bestehen, was nicht korrekt ist. Da Computer auf das Binär System basieren treffen die Zahlen nicht genau aufeinander. Das ist der Grund warum *eine 1 TB Festplatte* **nie einen ganzen TB Speicher** hat, sondern nur **931 GB**. 
![](Bild%209.png)

# Aufgabe 3: Konfiguration des HTTP Servers prüfen
Zuerst schaute ich ob ich das Problem nachkreieren konnte. Also öffnete ich den Browser auf dem Linux Client und gab `daskaffee.example` ein, das funktionierte gut. Dann gab ich `www.daskaffee.example` und es kam die Default-Seite von Apache2. Das heisst es muss an der Konfiguration liegen. Also schaute ich nach, wo die config-file für diese Seite ist. 
![](Bild%2010.png)

Unter `etc/apache2/sites-enabled` befindet sich eine Datei namens `001-daskaffe.conf`. Meine erste Vermutung war, dass der Domainname falsch eingetragen war, denn die URL `daskaffee.example` funktionierte. Also schaute ich in die Datei und erkannte, dass als Serveralias `daskaffee.example` stand. 
![](Bild%2011.png)

Der Tipp auf Gitlab sagte, dass eine Datei derselben Art für eine andere Webseite die richtige Zeile beinhaltet. Neben der config-file für die Seite `daskaffee.example` war auch noch eine config-file für die Seite `diefirma.example`. In dieser Datei gab es die Zeile Server Alias gar nicht, weshalb ich sie hinzufügte.
![](Bild%2012.png)

Dann den Apache Server neu starten und testen. 
![](Bild%2013.png)

# Aufgabe 4: Migration zu NGINX auf einem neuem Testserver
In der Aufgabe steht das Repository des Paketmanagers mit `apt update` zu updaten. Den Befehl hab ich ausgeführt. 
![](Bild%2014.png)
Dann nur noch `apt upgrade` eingeben, die Meldung akzeptieren und er macht das Upgrade. 
![](Bild%2015.png)

