- [Zurück zum README](../README.md) 

# Virtuelle Maschine erstellen
#### Instanz erstellen
Damit eine Windows Server VM erstellt werden kann, musste ich ich zuerst auf AWS einloggen. Danach unter EC2, der Service der Virtuelle Server in der Cloud, eine neue Instanz erstellen. 

<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/e5535ebc-9718-456d-9ccd-e7f1aca6ea6e">

#### Namen
Als nächstes den Namen der VM festlegen. Der Namen beeinflusst die Einstellungen der VM **nicht**. 

<img width="797" alt="name_vm" src="https://github.com/user-attachments/assets/ea0d3133-5b1d-441d-9cf7-e4afc3c4944d">

#### Operating System auswählen
In diesem Fall wählte ich Windows Server 2019. Es gibt auch andere Versionen. Die aktuellste ist die Windows Server Version aus dem Jahr 2022. 

<img width="803" alt="choose_os" src="https://github.com/user-attachments/assets/4a16b43d-5b91-4017-b3de-60d934f816c4">

#### Instance Type
Beim Instance Type wählte ich t2.micro, weil wenig Leistung benötigt wird. Es gäbe auch stärkere VM's, die aber kostenpflichtig sind. 

<img width="600" alt="instance_type" src="https://github.com/user-attachments/assets/e5772639-58c6-471b-b906-2c5b1516513a">

#### Key Pair erstellen
Hier muss man einen Key erstellen, mit dem der eigene Computer identifiziert werden kann. Dies dient der Anmeldung auf dem Server. 

<img width="801" alt="Key_Pair_Gen" src="https://github.com/user-attachments/assets/f747c5ea-fb25-4150-9362-552e58dcb02e">

#### Netzwerkeinstellungen 
Die Netzwerkeinstellungen kann man so lassen. Man könnte hier beispielsweise eine Regel für SSH oder HTTPS hinzufügen. 

<img width="600" alt="network_settings" src="https://github.com/user-attachments/assets/b54594ce-9998-4dfb-b6c8-fb4e0f46220a"> 

#### Beweis
Beim starten der Instanz muss man nur noch den vorher erhaltenen Private Key hochladen und kann sich beispielsweise per RDP auf den Server verbinden. 

<img width="600" alt="Beweis" src="https://github.com/user-attachments/assets/4b102dbf-c474-47d3-a97c-fde25f595f64">
