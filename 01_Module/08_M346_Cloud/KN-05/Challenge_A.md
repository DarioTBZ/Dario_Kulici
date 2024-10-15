
# VPC erstellen und Webserver darin deployen

### Was ist eine VPC?
Eine Virtual Private Cloud ist ein privates Netzwerk, das man komplett kontrolliert. Grundsätzlich ist es ein Firmen oder Heimnetzwerk, einfach in der Cloud. Man kann also Server oder sonstige Geräte in diesem Netzwerk isoliert betreiben. 

### VPC erstellen
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/b185e9fd-250b-44c4-98f1-b9a6b8db1c74">

Ich habe die VPC nach Vorgaben erstellt. 

### Instanz erstellen in VPC
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/0f49a22e-9b1c-42ad-870c-816038065eb4">

Danach erstelle ich die Instanz. Komischerweise zeigte es die Security group, die ich zuerst erstelle nicht an, weshalb ich sie auf dem Menu der Instanz erstelle musste. Deshalb bekam bei der **Benotung** (siehe unten) nicht die volle Punktzahl. 

<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/a58e7618-b6c4-46ab-941a-b970214a1bb8">

### Netzwerkeinstellungen der Instanz
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/d3a9ee95-5caf-4092-a9ca-ebde9d7ff63b">

Hier erkennt man die IP-Adresse der Instanz. Wichtig war hier, dass die Instanz nicht in der Standard-VPC erstellt wurde, sondern in dem VPC, das ich erstellt hatte. 

### Beweise
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/a906f172-a69c-4322-bc7d-6c849e5535f9">
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/75b3501f-fb2d-4c7e-85ba-dcdab50f39da">

Auf diesen Bildern erkennt man, die IP-Adresse und den Loadtest. 

### Fazit
Ich brauchte mehrere Versuche, bis ich die VPC richtig erstellt hatte. Anfangs verstand ich nicht ganz warum man vier Subnetze erstellen sollte. 

Jetzt denke ich, dass man die öffentlich zugänglichen Services im öffentlichen Subnetz deployed und das Backend von bspw. dem Webserver also eine Datenbank im privaten Subnetz. Die Privaten Subnetze können durch das NAT ins Internet und aber umgekehrt nicht gefunden werden. So erreicht man, dass die Datenbank nicht direkt über das Internet zugänglich ist. 

## Quellen
- [Was ist eine VPC? - ChatGPT](https://chatgpt.com/share/670e42b6-c5bc-8010-8804-c0788d0cee37) 
