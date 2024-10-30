# Load Balancer und Scaling Group mit Elasticy aufsetzen

### Launch Template erstellen
Als erstes erstelle ich das Launch Template. Unter advanced füge ich den neuen Code ein, der zusätzlich die Instanz ID ausgibt. 

Placeholder01

### Auto Scaling Group erstellen
Dann erstelle ich die Auto Scaling Group und benenne diese entsprechend der Aufgabe. Hierbei wichtig ist, dass das vorher erstellte Launch Template ausgewählt ist. Die Auto Scaling Group erstellt Instanzen nach diesem Template. 

Placeholder02

Die Group Size sieht so aus.

| Desired capacity | Min desired capacity | Max desired capacity |
| ---------------- | -------------------- | -------------------- |
| 2                | 2                    | 4                    |

Das heisst es werden bei wenig Auslastung minimum zwei Instanzen, normaler Auslastung zwei Instanzen und bei maximaler Auslastung maximal vier Instanzen genutzt. 

Placeholder03

Die Instanzen werden schon bei der Erstellung der Auto Scaling Group erstellt. Hier sieht man, dass sie erfolgreich deployed wurden. 

Placeholder04

### Target Group erstellen
Die Target Group dient dazu dem Load Balancer die Instanzen zu geben, auf die der traffic geleitet werden muss. Also wähle ich die zwei, von der Auto Scaling Group erstellten, Instanzen. 

Placeholder05

### Load Balancer
Als letztes muss nur noch der Load Balancer erstellt werden. Ich wähle die Security Group M346-KUL-Web-Access aus, nehme M346-KUL-VPC als VPC und wähle die vorher erstellte Target Group für die Weiterleitung aus. Auf dem Bild sieht man die Summary des Ganzen. 

Placeholder06

Der Load Balancer braucht ein wenig Zeit, um zu starten. Nach dem Starten muss er nur noch in der Auto Scaling Group erfasst werden. 

Placeholder07

### Dynamic Scaling Policy
Damit die Auto Scaling Group mehr Instanzen erstellt braucht es eine Dynamic Scaling Policy. Eine Dynamic Scaling Policy ist eine Voraussetzung, die falls sie erreicht wird mehr Instanzen erstellt. 

Placeholder08

Wenn die Seite 20x geladen wird, erstellt die Auto Scaling Group eine neue Instanz. Bis das definierte Maximum erreicht wird. 

Hier sieht man den Alarm und die erstellten Instanzen. 

Placeholder09
Placeholder10

### Fazit
Eine Dynamic Scaling Policy ist sehr effizient und vorteilhaft. Wenn mehr Benutzer auf eine Webseite zugreifen und die Leistung ans Maximum getrieben wird, ist es effizient mehr Instanzen zu erstellen. Es werden auch Kosten gespart, weil die Instanzen wieder gelöscht werden nachdem sie nicht mehr gebraucht werden. 