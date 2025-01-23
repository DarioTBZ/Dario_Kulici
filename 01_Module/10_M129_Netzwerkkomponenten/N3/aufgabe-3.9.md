# N3 Aufgabenstellung 3.9

### Vorgaben 
- Netzwerk mit Inter Vlan Routing

### Vorgehen

Ich verkabelte wieder die PCs mit dem Switch über Access Ports. Das letzte Interfaces des Switches verband ich über einen Trunk Port zum Router, damit der Verkehr von allen Vlans dort weitergeleitet wird. Auf dem Router erstellte ich die Sub Interfaces für alle Vlans, aktivierte die Enkapsulierung und wendete die Änderungen mit write memory an. 

Das Vlan 50 musste ich auf dem Router logischerweise auf dem zweiten Interface erstellen, weil der Switch auf dem zweiten Interfaces des Routers ist. Also anstatt interface g 0/0.50 ist der richtige Befehl interface g 0/1.50. 

### Switch Config

<img width=50% height=50% alt="SwitchVlans" src="">

### Router Config

<img width=50% height=50% alt="Routerconfig" src="">

### Fazit

Zusammenfassend kann ich sagen, dass ich verstanden habe wie Vlans funktionieren. Dennoch verstehe ich nicht wie man Inter Vlan Routing aktiviert oder deaktiviert. In der Übung 3.8 musste man das Netzwerk ohne Inter Vlan Routing erstellen und hier bei 3.9 mit. Die Herangehensweise der beiden Übungen war genau gleich. Das heisst ich habe hier bei 3.9 genau das gleiche wie auf 3.8 gemacht. 