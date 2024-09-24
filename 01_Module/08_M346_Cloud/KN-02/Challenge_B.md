# Zugriff auf Instanz mit SSH-Key

### Instanz Details
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/a7c2ad81-9b8f-41c3-846a-d033578d195c">

Hier sieht man, dass ich Dario-1 als Key ausgewählt habe. 

### Erster Key
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/b2fb3e4b-5cea-4917-8ae2-3021920b74ef">

Die Private Keys habe ich in einen Ordner platziert und die Berechtigungen angepasst, sodass nur mein User Zugriff darauf hat. 

Der Zugriff auf die Instanz hat sauber funktioniert. 

### Zweiter Key
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/39afac5a-9b4f-4989-b73a-5d55141170c0">

Mit dem zweiten Key, der im selben Ordner ist, hat der Zugang *nicht funktioniert* Auf der Instanz habe ich den Key Dario-1 ausgewählt. Der zweite Key wird gar **nicht verwendet**, weshalb er auch **nicht funktioniert**. 

Erst wenn er auf der Instanz ausgewählt wird, kann er funktionieren, weil die Instanz erst dann auf einen anderen Key hört. 
