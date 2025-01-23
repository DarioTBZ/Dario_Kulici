# N3 Aufgabenstellung 3.8

### Vorgaben
- Ohne Inter Vlan Routing


### Vorgehen

Als erstes verkabelte ich alle Interfaces vom Switch zu den richtigen PCs. Danach erstellte ich die Vlans auf dem Switch. Die Abteilungen erhalten jeweils zwei Access Interfaces. Das letzte Interfaces, was zum Router geht ist auf Trunk eingestellt, damit er alle Vlans durchlässt. Auf dem Router erstellte ich die Sub Interfaces nach Vorgabe, die 802.1Q Enkapsulierung aktiviert und die Änderungen mit ``write-memory`` angewendet. 

#### Switch Config

Hier sieht man die erstellten Vlans. 

<img width=50% height=50% alt="SwitchVlans" src="https://github.com/user-attachments/assets/989946b8-388a-4c7b-a6b6-c814586b3c76">

#### Router Config

Auf diesem Bild sieht man die angewendeten Befehle. Zusätzlich überprüfte ich mit ``show running-config`` die aktuelle Konfiguration und sicherte die Konfiguration mit ``write-memory``.

<img width=50% height=50% alt="RouterConfig" src="https://github.com/user-attachments/assets/b03b1d16-7e73-4a9c-bdee-d70e6a417373">

### Troubleshooting

Anfangs haben alle Vlans miteinander kommunizieren können, was ja nicht sein sollte. Da **fand ich erst heraus**, dass die Config **gesichert werden musste**, damit die Änderungen gespeichert werden. Danach funktionierte es. 

### Testing

Ping von Vlan 10 zu anderen PC:

<img width=50% height=50% alt="Vlan10" src="https://github.com/user-attachments/assets/f0c67bfd-3059-446b-8793-30ccd98ff5cb">

Ping von Vlan 20 zu anderen PC:

<img width=50% height=50% alt="Vlan20" src="https://github.com/user-attachments/assets/cd5b7c38-aca6-41c1-a7c7-75e979bb2ad9">

### Fazit 

Das Wichtigste war, die Router Config zu speichern, damit die Änderungen übernommen werden. 
