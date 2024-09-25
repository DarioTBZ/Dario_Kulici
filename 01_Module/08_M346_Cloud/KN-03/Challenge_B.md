# Instanz mit Cloud-Init deployen

### Cloud-Init Config Datei
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/3a0e2c5c-4394-40da-9d1d-fc7e10ee8ebc">

Das ist die Cloud-Init Datei. Sie ist auch im Repository abgelegt. 

### Verwendete Key
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/f3760349-00f2-4505-933b-2654a362b26e">

Auf dem Bild sieht man, dass Dario-2 als Key verwendet wurde. In der Cloud-Init Datei ist der Public Key von der Dario-1.pem Datei. 

### SSH Login mit ersten Key
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/af3d1127-df40-4502-a796-6e6d0cc2798f">

Der Zugriff mit dem ersten Key gelingt, weil er auch in der Cloud-Init Datei als authorized_key angegeben wurde. 

### SSH Login mit zweiten Key
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/20857fc2-613f-4a46-970f-d1178e47dbc6">

Der Zugriff schlägt fehl, weil der zweite Schlüssel von der Cloud-Init Config überschrieben wurde. 

### Cloud-Init Log
<img width=50% height=50% alt="launch_instance" src="https://github.com/user-attachments/assets/38190a0c-ec36-4c69-89fd-f8b53d5c3794">

Hier erkennt man, dass die Cloud-Init Config erfolgreich war. Wget und Curl wurden installiert, was heisst, dass die Config war komplett erfolgreich. 

# Mehrere Keys hinterlegen
Es können natürlich mehrere Computer auf diese Instanz zugreifen. Dafür muss der Public Key von der Maschine, die Zugriff benötigt auf der Instanz unter authorized_keys eingetragen werden. 