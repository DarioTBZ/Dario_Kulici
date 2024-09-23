# Virtualisierung

#### Begriff 
Virtualisierung ist eine Abstraktion der physischen Hardware-Ressourcen. Somit können auf einem Betriebssystem mehrere virtuelle Maschinen laufen. Dies ist Ressourcenaufwendig aber eine effiziente Methode, weil ganze Betriebssysteme simuliert werden. Virtuelle Maschinen können leicht gesichert und in einem Notfall wiederhergestellt werden. 

#### Hypervisor
Ein Hypervisor ist eine Applikation, die als "Manager" von virtuellen Maschinen dient. Sie weist Ressourcen von der physischen Hardware zu den laufenden Maschinen zu. 

##### Type 1
Es gibt Type 1 Hypervisors, die direkt auf dem System installiert werden. Das heisst man installiert nicht Windows oder Linux sondern den Type 1 Hypervisor, der die virtuellen Maschinen verwaltet. Dies nennt man meistens einen eingebetteten oder gehosteter Hypervisor. 

##### Type 2
Ein Beispiel für einen Type 2 Hypervisor ist die VMware Workstation. Diese Art von Hypervisor wird auf einem bestehenden Betriebssystem installiert und hat keinen direkten Zugriff auf die Hardware-Ressourcen. 

#### Hyperscaler
Ein Hyperscaler bietet grössere und flexiblere Rechenzentren als herkömmliche Rechenzentren an. Der Hauptunterschied ist dabei, dass wenn mehr Leistung benötigt wird, diese sofort zur Verfügung gestellt werden kann. Bei einem normalen Rechenzentrum müsste man warten bis die Hardware verfügbar ist oder erst installiert wird. 

![Hyperscaler_Bild](https://github.com/user-attachments/assets/c678d07a-af49-4da0-ae6a-1d6792d3993d)

#### Cloud-System Schichten
[Siehe Servicemodelle](02_Servicemodelle.md) 

## Quellen
- [Begriff Erklärung](https://it-service.network/it-lexikon/virtualisierung/#:~:text=Unter%20dem%20Begriff%20Virtualisierung%20ist,von%20verschiedenen%20Nutzern%20verwendet%20werden.) 
- [Hypervisor Type 1 & 2](https://aws.amazon.com/de/compare/the-difference-between-type-1-and-type-2-hypervisors/) 
- [Hyperscaler](https://www.redhat.com/de/topics/cloud-computing/what-is-a-hyperscaler) 
