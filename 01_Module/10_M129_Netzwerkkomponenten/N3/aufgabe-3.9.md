# N3 Aufgabenstellung 3.9

### Vorgaben 
- Netzwerk mit Inter Vlan Routing

### Vorgehen

Ich verkabelte wieder die PCs mit dem Switch über Access Ports. Das letzte Interfaces des Switches verband ich über einen Trunk Port zum Router, damit der Verkehr von allen Vlans dort weitergeleitet wird. Auf dem Router erstellte ich die Sub Interfaces für alle Vlans, aktivierte die Enkapsulierung und wendete die Änderungen mit write memory an. 

Das Vlan 50 musste ich auf dem Router logischerweise auf dem zweiten Interface erstellen, weil der Switch auf dem zweiten Interfaces des Routers ist. Also anstatt interface g 0/0.50 ist der richtige Befehl interface g 0/1.50. 

### Switch Config

<img width=50% height=50% alt="Switch0Vlans" src="https://github.com/user-attachments/assets/26654672-fd60-4693-af92-773e3c8a1f58">
<img width=50% height=50% alt="Switch1Vlans" src="https://github.com/user-attachments/assets/823c9ae9-7575-4929-bb91-0d0b9b3c9a43">

### Router Config

<img width=50% height=50% alt="Routerconfig" src="https://github.com/user-attachments/assets/55f4c03c-f379-4c42-bf07-d44bb754ccdb">


### Testing

Verschiedene PDUs:

<img width=50% height=50% alt="PDUs" src="https://github.com/user-attachments/assets/34dd7d91-01fa-4760-8f11-3357f67795c5">

Ping von PC-11 zu PC-51:

<img width=50% height=50% alt="Ping" src="https://github.com/user-attachments/assets/e2ce95f5-f55d-43dd-bed1-04d6ef908595">

### Fazit

Zusammenfassend kann ich sagen, dass ich verstanden habe wie Vlans funktionieren. Dennoch verstehe ich nicht wie man Inter Vlan Routing aktiviert oder deaktiviert. In der Übung 3.8 musste man das Netzwerk ohne Inter Vlan Routing erstellen und hier bei 3.9 mit. Die Herangehensweise der beiden Übungen war genau gleich. Das heisst ich habe hier bei 3.9 genau das gleiche wie auf 3.8 gemacht. 
