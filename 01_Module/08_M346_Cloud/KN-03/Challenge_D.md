# Trennung von Web- und Datenbankserver

Wenn man einen Datenbankserver hat, der viel Leistung verbraucht und der Webserver auf der gleichen Maschine läuft. Kann das System irgendwann mal schlecht laufen. Dazu kommt wenn man beispielsweise mit dem Webserver ein Problem hat und die Maschine neu starten muss, wird auch der Datenbankserver neu gestartet. Dies kann eine länger Downtime bedeuten und man verliert möglicherweise Kunden. Aus diesen Gründen splittet man diese zwei Anwendungen auf zwei Maschinen bzw. Instanzen wenn man in der Cloud arbeitet. 

## Datenbankserver

### Admin Login auf Datenbank
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/f5ec97eb-abe9-4a54-aa64-35b277ec2407">
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/efdb8cc4-ff24-4e40-9390-19bcb87b6831">

Auf den Bildern erkennt, man das erfolgreiche Login auf den Admin Account. Damit es aber dazu kam, musste ich mich zuerst mit dem Root anmelden und das Admin Passwort ändern. Nach einer kurzen Recherche fand ich es heraus und konnte mich dann erfolgreich anmelden. 

### Per Telnet Port testen
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/ae84cf1c-10fc-4417-a5a8-8dd1436bcd45">

Der Port ist offen und es kam eine kryptische Nachricht zurück. So weiss man, dass der Port offen ist und funktioniert. 

## Webserver 

### index.html
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/e5481e1d-0f10-44a2-b9c8-a72c8adfb639">

Bild der Index.html Datei. 

### info.php
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/ba4f4d20-b4bb-4a85-b080-9c3d5ef7a765">

Bild der info.php Datei.

### db.php
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/6c5b2347-1f14-4ac3-a902-9024381e9a45">

Hier war wichtig, dass die Login Daten und die IP Adresse der Datenbank richtig eingetragen sind, weil sonst nichts angezeigt werden würde. 


## Cloud-Init Datei

| Befehl          | Wert         | Auswirkung                                                 |
| --------------- | ------------ | ---------------------------------------------------------- |
| users           | -            | User können hier erfasst werden.                           |
| name            | String       | Name des Users                                             |
| sudo            | String       | Ob dieser User ein Sudoer sein darf.                       |
| groups          | String       | Gruppen, in denen der User sein soll.                      |
| home            | String       | Das Homeverzeichnis des Users.                             |
| shell           | String       | Standard Shell                                             |
| ssh_pwauth      | True / False | Ob man sich per SSH mit Passwort einloggen kann.           |
| disbale_root    | True / False | Ob der Root Account deaktiviert werden soll.               |
| package_update  | True / False | Ob die fehlenden Paketupdates herunterladen werden sollen. |
| package_upgrade | True / False | Ob die Updates angewendet werden sollen.                   |
| packages        | String       | Welche zusätzlichen Pakete heruntergeladen werden sollen.  |
| runcmd          | String       | Welche Befehle ausgeführt werden sollen.                   |
| write_files     | String       | Was für Dateien wo erstellt werden.                        |


## Fazit
Ich habe anfangs sehr viel Fehler gemacht. Die Cloud-Init Datei war die ersten vier Instanzen falsch und ich habe es erst dann bemerkt, dank der cloud-init-output Datei. Der SSH Key war auch zuerst falsch formatiert und war erst später richtig. 

Am Schluss  hab ich mich auf jeden Fall sehr gefreut, dass ich es geschafft habe. 
