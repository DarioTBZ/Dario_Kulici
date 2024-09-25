# Trennung von Web- und Datenbankserver

Wenn man einen Datenbankserver hat, der viel Leistung verbraucht und der Webserver auf der gleichen Maschine läuft. Kann das System irgendwann mal schlecht laufen. Dazu kommt wenn man beispielsweise mit dem Webserver ein Problem hat und die Maschine neu starten muss, wird auch der Datenbankserver neu gestartet. Dies kann eine länger Downtime bedeuten und man verliert möglicherweise Kunden. Aus diesen Gründen splittet man diese zwei Anwendungen auf zwei Maschinen bzw. Instanzen wenn man in der Cloud arbeitet. 

## Datenbankserver

### Admin Login auf Datenbank
Placeholder

Auf dem Bild erkennt, man das erfolgreiche Login auf den Admin Account. Damit es aber dazu kam, musste ich mich zuerst mit dem Root anmelden und das Admin Passwort ändern. Nach einer kurzen Recherche fand ich es heraus und konnte mich dann erfolgreich anmelden. 

### Per Telnet Port testen
Placeholder

Der Port ist offen und es kam eine kryptische Nachricht zurück. So weiss man, dass der Port offen ist und funktioniert. 

## Webserver 

### index.html
Placeholder

Bild der Index.html Datei. 

### info.php
Placeholder

Bild der info.php Datei.

### db.php
Placeholder

Hier war wichtig, dass die Login Daten und die IP Adresse der Datenbank richtig eingetragen sind, weil sonst nichts angezeigt werden würde. 

### adminer
Placeholder

Hier auch das Login der Datenbank nutzen. 

## Fazit
Ich habe anfangs sehr viel Fehler gemacht. Die Cloud-Init Datei war die ersten vier Instanzen falsch und ich habe es erst dann bemerkt, dank der cloud-init-output Datei. Der SSH Key war auch zuerst falsch formattiert und war erst später richtig. 

Am Schluss  hab ich mich auf jeden Fall sehr gefreut, dass ich es geschafft habe. 