### Zwei Webserver Instanzen erstellen
Ich erstellte als erstes eine simple Webserver Instanz. Dabei musste ich eine Security Group erstellen, die den HTTP traffic vom Internet erlaubt. Zusätzlich fügte ich unter "Advanced" Linux Befehle ein, die die Webserver-Applikation Apache2 herunterladen und den Dienst starten. 

Nachdem die Instanz gestartet wurde wählte ich unter "Aktion" die Option "Launch more like this". Dies leitete mich zu einem Fenster, auf dem die Konfiguration von der gewählten Instanz übernommen wurde. Ich musste lediglich den Name der Instanz ändern, den Key nochmals auswählen, den Code unter "Advanced" anpassen und konnte die Instanz schon starten. 

<img width=50% height=50% alt="Placeholder1" src="https://github.com/user-attachments/assets/284d8e14-70fe-4b9d-9f0f-9a9a12e3802c">

Nachdem die zwei Instanzen vollständig gestartet waren, öffnete ich die öffentliche IP-Adresse. Auf beiden Instanzen erkannte man die erstellte HTML Webseite. 

<img width=50% height=50% alt="Placeholder2" src="https://github.com/user-attachments/assets/bf629eb6-4d3c-45be-b6f6-f81d5dd623e8">

### Load Balancer erstellen
Unter "Load Balancers" wählte ich die Option Application Load Balancer. Dieser kann HTTP(S) Anfragen effizient und intelligent verarbeiten. 

<img width=50% height=50% alt="Placeholder3" src="https://github.com/user-attachments/assets/b147ed44-c86b-453c-80df-6e065d845572">

Als nächstes wählte ich den "target type" "Instances" und setzte den Namen fest. 

<img width=50% height=50% alt="Placeholder4" src="https://github.com/user-attachments/assets/0f278ffd-576f-43de-965c-6a4d656e0052">

Hier unter "Register targets" muss ich die erstellten Instanzen auswählen. 

<img width=50% height=50% alt="Placeholder5" src="https://github.com/user-attachments/assets/ddc34725-b790-4d29-b719-c04bbc0a0abe">

Das hier ist die Übersicht von der **Target Group**. Eine Target Group empfängt den einkommenden definierten traffic und leitet ihn an die dementsprechenden Instanzen weiter. In diesem Fall ist es HTTP also Port 80. 

<img width=50% height=50% alt="Placeholder6" src="https://github.com/user-attachments/assets/fa0bae07-0ac8-4273-809d-1e2e0474483f">

Um die Load Balancer Konfiguration abzuschliessen muss die Target Group nur noch dem Load Balancer hinzugefügt werden. Dieser ist nach einigen Minuten bereit. 

<img width=50% height=50% alt="Placeholder7" src="https://github.com/user-attachments/assets/fcd10ab8-539f-48f7-98a2-9daee02a5a79">

Das Beweisvideo ist hier auf der Repo hochgeladen. Da ich das Lab beenden muss, wird alles gelöscht. 


[Beweis Video](https://github.com/user-attachments/assets/74646616-6807-4a59-8b70-e4312b772e75)


### Fazit
Ein Load Balancer ist sehr effektiv. Jetzt da ich weiss, wie dieser funktioniert und aufgesetzt wird, bin ich gespannt, wie es weiter geht. 
