### Aufgabe 1: High Availability
Beschreiben Sie anhand von folgenden zwei Use-Cases, welche **HA-Massnahmen** sie jeweils präventiv umsetzen würden. 

- **Stromausfall**
- **Erdbeben** 

##### Lösung
Damit bei einem Stromausfall die Availability bleibt, würde ich mehrere Stromquellen nutzen. Das heisst sobald eine Stromquelle ausfällt hat man noch eine oder mehrere andere. Ein Beispiel für "Backup-Strom" wäre eine USV. Falls ein Erdbeben dort auftauchen würde, wo eine Firma alle Ihre Server hat, hätte die Firma ein riesiges Problem. Deswegen würde ich mehrere Datenzentren an verschiedenen Orten haben, damit falls ein Erdbeben oder eine sonstige Katastrophe auftauchen würde, nicht alle Server verloren wären. 

---

### Aufgabe 2: Fault Tolerance
Erklären Sie anhand von **drei** Beispielen, welche **Redundanzen** Sie einführen würden, wenn Sie verantwortlich wären für einen **kleinen Serverraum** einer Kleinfirma.  

- Redundanz einführen
- Load Balancing verwenden
- Geografische Verteilung / Failover-Regionen

Überlegen Sie sich, ob und wie dieselben Redundanzen bei einem Cloud-Provider umgesetzt werden. (Halten sie diese Gedanken ebenfalls mit ein paar eigenen Sätzen in Ihrem Repo unter KN06 A) fest. 

##### Lösung
Damit die fault tolerance so *tief wie möglich* bleibt, würde ich erstens eine **USV** für Backup-Strom verwenden und zweitens einen **zweiten Netzwerkanschluss** verwenden (anderer Anbieter). Falls der Strom ausfällt würde der Serverraum noch etwas länger laufen, da er den Strom über die USV bekommen würde. Das gleiche Prinzip erreicht man, indem man zwei Netzwerkanschlüsse von zwei verschiedenen Anbietern (ISP) hat. Falls ein Anbieter einen Ausfall haben würde wäre der Serverraum über den anderen erreichbar. 

Bei einem Cloud-Provider werden höchstwahrscheinlich die selben Massnahmen getroffen, weil die Datenzentren auch Netzwerk und Strom brauchen. Das Netzwerk bei einem Cloud-Provider hat einen anderen Aufbau, weshalb es eine kompliziertere Sache wäre, aber das Prinzip grundsätzlich gleich bleibt. 



### Aufgabe 3: Load Balancer
Es gibt drei Typen von load balancer, die alle einen eigenen Zweck haben.

- Application Load Balancer (ALB)
- Network Load Balancer (NLB)
- Gateway Load Balancer (GWLB)

##### Application Load Balancer
Ein application load balancer arbeitet auf einer application layer (7) und ist am besten geeignet für Applikationen. Er leitet HTTP(S) Anfragen intelligent verarbeiten und ist deshalb sehr nützlich für Webanwendungen, bei denen die Anfragen gezielt weitergeleitet werden müssen. 

##### Network Load Balancer
Der network load balancer regelt den traffic, wie der Name schon sagt, auf Netzwerkebene. Er kann extrem viele Anfragen gleichzeitig weiterleiten und ist ideal für Weiterleitungen mit niedriger Latenz. 

##### Gateway Load Balancer
Der gateway load balancer arbeitet auf Layer 3. Er verteilt den traffic basierend auf IP-Adressen und Gruppenregeln. Dieser load balancer ist geeignet für Sicherheit und Netzwerküberwachung. 

###### EC2 Instanz Gesundheit
Jeder load balancer entscheidet welche EC2 Instanz am gesundesten ist und leitet den traffic dorthin weiter. Am gesundesten ist eine EC2 Instanz, wenn sie eine geringe Latenz hat und betriebsbereit ist. AWS überprüft regelmässig ob eine Instanz gesund ist. 

#### Auto Scaling und Load Balancer
Um eine hohe Skalierbarkeit und Verfügbarkeit zu erreichen kann man den Auto-Scaling-Service von AWS mit einem Load Balancer **kombinieren**. Somit werden EC2 Instanzen je nach **Nachfrage gelöscht oder erstellt** und ein Load Balancer *verteilt den traffic basierend auf den bestehenden Instanzen*. Damit bösartige Attacken wie z.B eine **DDoS-Attacke verhindert** werden kann nutzt man den **Cloud-Watch Service** von AWS. Dieser überwacht bspw. CPU-Auslastung und Speicher und gibt einen **Alarm** aus, falls er auffällige Muster erkennt. Somit kann mit Cloud-Watch die Leistung von Load Balancers überwacht und bei Bedarf optimiert werden. 



### Aufgabe 4: Auto-Scaling
Amazon Auto-Scaling skaliert Instanzen je nach Richtlinie. Beispielsweise kann man den Auto-Scaler so einstellen, dass er sobald die CPU-Auslastung von EC2 Instanzen zu hoch wird, eine oder mehrere neue Instanzen erstellt. Genauso kann er Instanzen bei geringer Nutzung löschen, um Ressourcen und Geld zu sparen. Eine andere Richtlinie wäre die geplante Skalierung. Hier definiert man wann wie viele Instanzen laufen sollen. Wenn man beispielsweise weiss, dass um 0:00 bis 6:00 Morgens wenig Anfragen kommen, wird die Anzahl Instanzen auf ein **Minimum reguliert**. Insgesamt gibt es noch ein paar weitere Richtlinien, aber je nach Situation oder Wunsch kann eine passende Richtlinie gewählt werden. 

Ein Load Balancer mit einem Auto-Scaler kombiniert ist sehr effektiv. Der Load Balancer verteilt den traffic an die verschiedenen Instanzen je nach Anzahl. Somit werden Ressourcen gespart und die Effizient gesteigert. 