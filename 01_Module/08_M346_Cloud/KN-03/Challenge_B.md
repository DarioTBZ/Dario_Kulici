# Instanz mit Cloud-Init deployen

### Cloud-Init Config Datei
Placeholder

Das ist die Cloud-Init Datei. Sie ist auch im Repository abgelegt. 

### Verwendete Key
Placeholder

Auf dem Bild sieht man, dass Dario-2 als Key verwendet wurde. In der Cloud-Init Datei ist der Public Key von der Dario-1.pem Datei. 

### SSH Login mit ersten Key
Placeholder

Der Zugriff mit dem ersten Key gelingt, weil er auch in der Cloud-Init Datei als authorized_key angegeben wurde. 

### SSH Login mit zweiten Key
Placeholder

Der Zugriff schlägt fehl, weil der zweite Schlüssel von der Cloud-Init Config überschrieben wurde. 

### Cloud-Init Log
Placeholder

Hier erkennt man, dass die Cloud-Init Config erfolgreich war. Wget und Curl wurden installiert, was heisst, dass die Config war komplett erfolgreich. 