# Snapshot von EBS Volume erstellen und wieder restoren

### EBS Volume erstellen
Ich erstelle das EBS Volume und attache es der Lab Instanz. 

Placeholder01

Wenn man `df` eingibt, also die Dateisystemes ausgibt ist das zugewiesene Volume noch nicht zu sehen. Also erstelle ich das Filesystem. 

Placeholder02

Danach erstelle ich einen Ordner im Mount Ordner und mounte das erstellte Filesystem. Auf dem Bild sieht man, das erschienene `dev/xvdf`, das auf data-store gemounted wurde. 

Placeholder03

Als nächstes erstelle ich eine Datei mit Inhalt, die dann gesichert wird. 

Placeholder04

Hier erstelle ich einen Snapshot des Volumes. 

Placeholder06

Zum testen lösche ich die Datei auf der Instanz. 

Placeholder06

### Restore vom Snapshot

Von diesem Snapshot erstelle ich ein Volume, welches dann auf die Instanz gemounted wird. 

Placeholder07

Das mounte ich und siehe da die Datei ist noch vorhanden. 

Placeholder08

### Fazit
Snapshots sind eine effiziente Möglichkeit Volumen zu sichern. Bei einem Ausfall oder Fehler kann man jederzeit den letzten Snapshot restoren. 