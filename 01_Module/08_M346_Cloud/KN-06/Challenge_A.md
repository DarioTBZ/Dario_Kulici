---
tags:
  - KN
---
### Aufgabe 1: High Availability
Beschreiben Sie anhand von folgenden zwei Use-Cases, welche **HA-Massnahmen** sie jeweils präventiv umsetzen würden. 

- **Stromausfall**
- **Erdbeben** 

##### Lösung
Damit bei einem Stromausfall die Availability bleibt, würde ich mehrere Stromquellen nutzen. Das heisst sobald eine Stromquelle ausfällt hat man noch eine oder mehrere andere. Ein Beispiel für "Backupstrom" wäre eine USV. 

### Aufgabe 2: Fault Tolerance
Erklären Sie anhand von **drei** Beispielen, welche **Redundanzen** Sie einführen würden, wenn Sie verantwortlich wären für einen **kleinen Serverraum** einer Kleinfirma.  

Überlegen Sie sich, ob und wie dieselben Redundanzen bei einem Cloud-Provider umgesetzt werden. (Halten sie diese Gedanken ebenfalls mit ein paar eigenen Sätzen in Ihrem Repo unter KN06 A) fest. 

##### Lösung
Damit die Fault Tolerance so *tief wie möglich* bleibt, würde ich erstens eine **USV** für Backupstrom verwenden und zweitens einen **zweiten Netzwerkanschluss** verwenden (anderer Anbieter). Falls der Strom ausfällt würde der Serverraum noch etwas länger laufen, da er den Strom über die USV bekommen würde. Das gleiche Prinzip erreicht man, indem man zwei Netzwerkanschlüsse von zwei verschiedenen Anbietern (ISP) hat. Falls ein Anbieter einen Ausfall haben würde könnte der Serverraum über den anderen erreichbar sein. 

Bei einem Cloud-Provider werden höchstwahrscheinlich auch diese Massnahmen getroffen, weil die Datenzentren auch Netzwerk und Strom brauchen. Das Netzwerk hat einen anderen Aufbau, weshalb es eine kompliziertere Sache ist, aber grundsätzlich ist das Prinzip gleich. 

### Aufgabe 3: Load Balancer
Es gibt drei Typen von Load Balancer, die alle einen eigenen Zweck haben.

- Application Load Balancer (ALB)
- Network Load Balancer (NLB)
- Gateway Load Balancer (GWLB)

##### Application Load Balancer
Dieser Load Balancer verteilt den traffic anhand vom Inhalt. Deswegen ist er geeignet für Webanwendungen. 