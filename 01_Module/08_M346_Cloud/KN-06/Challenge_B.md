### Zwei Webserver Instanzen erstellen
Ich erstellte als erstes eine simple Webserver Instanz. Dabei musste ich eine Security Group erstellen, die den HTTP traffic vom Internet erlaubt. Zusätzlich fügte ich unter "Advanced" Linux Befehle ein, die die Webserver-Applikation Apache2 herunterladen und den Dienst starten. 

Nachdem die Instanz gestartet wurde wählte ich unter "Aktion" die Option "Launch more like this". Dies leitete mich zu einem Fenster, auf dem die Konfiguration von der gewählten Instanz übernommen wurde. Ich musste lediglich den Name der Instanz ändern, den Key nochmals auswählen, den Code unter "Advanced" anpassen und konnte die Instanz schon starten. 

Placeholder01

Nachdem die zwei Instanzen vollständig gestartet waren, öffnete ich die öffentliche IP-Adresse. Auf beiden Instanzen erkannte man die erstellte HTML Webseite. 

Placeholder02

### Load Balancer erstellen
Unter "Load Balancers" wählte ich die Option Application Load Balancer. Dieser kann HTTP(S) Anfragen effizient und intelligent verarbeiten. 

Placeholder03

