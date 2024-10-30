# Load Balancer und Scaling Group mit Elasticy aufsetzen

### Launch Template erstellen
Als erstes erstelle ich das Launch Template. Unter advanced füge ich den neuen Code ein, der zusätzlich die Instanz ID ausgibt. 

<img width=50% height=50% alt="Placeholder01" src="https://github.com/user-attachments/assets/e391d71f-5ac1-41ec-988a-a971b04a879f">

### Auto Scaling Group erstellen
Dann erstelle ich die Auto Scaling Group und benenne diese entsprechend der Aufgabe. Hierbei wichtig ist, dass das vorher erstellte Launch Template ausgewählt ist. Die Auto Scaling Group erstellt Instanzen nach diesem Template. 

<img width=50% height=50% alt="Placeholder02" src="https://github.com/user-attachments/assets/4a06a58e-36da-4040-b79c-a4296733d509">

Die Group Size sieht so aus.

| Desired capacity | Min desired capacity | Max desired capacity |
| ---------------- | -------------------- | -------------------- |
| 2                | 2                    | 4                    |

Das heisst es werden bei wenig Auslastung minimum zwei Instanzen, normaler Auslastung zwei Instanzen und bei maximaler Auslastung maximal vier Instanzen genutzt. 

<img width=50% height=50% alt="Placeholder03" src="https://github.com/user-attachments/assets/b20a8f10-32b0-4be0-b856-0eaa53b436bb">

Die Instanzen werden schon bei der Erstellung der Auto Scaling Group erstellt. Hier sieht man, dass sie erfolgreich deployed wurden. 

<img width=50% height=50% alt="Placeholder04" src="https://github.com/user-attachments/assets/c7abf418-ff00-471f-9a25-07e5afbec701">

### Target Group erstellen
Die Target Group dient dazu dem Load Balancer die Instanzen zu geben, auf die der traffic geleitet werden muss. Also wähle ich die zwei, von der Auto Scaling Group erstellten, Instanzen. 

<img width=50% height=50% alt="Placeholder05" src="https://github.com/user-attachments/assets/c3ed80e2-1bb4-43c2-a848-7b6381e64fc0">

### Load Balancer
Als letztes muss nur noch der Load Balancer erstellt werden. Ich wähle die Security Group M346-KUL-Web-Access aus, nehme M346-KUL-VPC als VPC und wähle die vorher erstellte Target Group für die Weiterleitung aus. Auf dem Bild sieht man die Summary des Ganzen. 

<img width=50% height=50% alt="Placeholder06" src="https://github.com/user-attachments/assets/5b9363b0-580e-4bb5-9674-02cd305335ba">

Der Load Balancer braucht ein wenig Zeit, um zu starten. Nach dem Starten muss er nur noch in der Auto Scaling Group erfasst werden. 

<img width=50% height=50% alt="Placeholder07" src="https://github.com/user-attachments/assets/05e46da2-4fbb-4c2f-bf50-4b6dc906345d">

### Dynamic Scaling Policy
Damit die Auto Scaling Group mehr Instanzen erstellt braucht es eine Dynamic Scaling Policy. Eine Dynamic Scaling Policy ist eine Voraussetzung, die falls sie erreicht wird mehr Instanzen erstellt. 

<img width=50% height=50% alt="Placeholder08" src="https://github.com/user-attachments/assets/08270991-93c2-4343-860b-24c005b7d0a4">
Wenn die Seite 20x geladen wird, erstellt die Auto Scaling Group eine neue Instanz. Bis das definierte Maximum erreicht wird. 

Hier sieht man den Alarm und die erstellten Instanzen. 

<img width=50% height=50% alt="Placeholder09" src="https://github.com/user-attachments/assets/0ca83860-c2d0-4002-ad75-3c762b931eed">
<img width=50% height=50% alt="Placeholder10" src="https://github.com/user-attachments/assets/66607a55-585d-4fe5-a140-905ce1458283">

### Fazit
Eine Dynamic Scaling Policy ist sehr effizient und vorteilhaft. Wenn mehr Benutzer auf eine Webseite zugreifen und die Leistung ans Maximum getrieben wird, ist es effizient mehr Instanzen zu erstellen. Es werden auch Kosten gespart, weil die Instanzen wieder gelöscht werden nachdem sie nicht mehr gebraucht werden. 
