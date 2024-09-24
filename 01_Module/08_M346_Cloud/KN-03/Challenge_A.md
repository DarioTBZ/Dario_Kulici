# Cloud Init

### Yaml Config Datei
``` 
#cloud-config
users:
  - name: ubuntu
    sudo: ALL=(ALL) NOPASSWD:ALL
    groups: users, admin
    home: /home/ubuntu
    shell: /bin/bash
    ssh_authorized_keys:
      - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC0WGP1EZykEtv5YGC9nMiPFW3U3DmZNzKFO5nEu6uozEHh4jLZzPNHSrfFTuQ2GnRDSt+XbOtTLdcj26+iPNiFoFha42aCIzYjt6V8Z+SQ9pzF4jPPzxwXfDdkEWylgoNnZ+4MG1lNFqa8aO7F62tX0Yj5khjC0Bs7Mb2cHLx1XZaxJV6qSaulDuBbLYe8QUZXkMc7wmob3PM0kflfolR3LE7LResIHWa4j4FL6r5cQmFlDU2BDPpKMFMGUfRSFiUtaWBNXFOWHQBC2+uKmuMPYP4vJC9sBgqMvPN/X2KyemqdMvdKXnCfrzadHuSSJYEzD64Cve5Zl9yVvY4AqyBD aws-key       
ssh_pwauth: false
disable_root: false 
package_update: true
packages:
  - curl 
  - wget 
```


| Variable            | Wert         | Erklärung                                                        |
| ------------------- | ------------ | ---------------------------------------------------------------- |
| name                | String       | Definiert den Hostnamen.                                         |
| sudo                | String       | Definiert welche User Adminrechte habe.                          |
| groups              | String       | Definiert die Gruppen.                                           |
| home                | Path         | Definiert das Homeverzeichnis.                                   |
| shell               | Path         | Definiert die Defaultshell.                                      |
| ssh_authorized_keys | String       | Definiert Keys, die per SSH Zugang zur Maschine haben dürfen.    |
| ssh_pwauth          | True / False | Definiert ob man sich bei SSH mit einem Passwort einloggen kann. |
| disable_root        | True / False | Definiert ob man sich beim Root anmelden kann.                   |
| package_update      | True / False | Definiert ob die installierten Pakete aktualisiert werden.       |
| packages            | String       | Definiert was für Pakete heruntergeladen werden sollen.          |

### Beispiel
Dies ist ein Beispiel was der Wert `package_update` ausmacht. Wenn der Wert `package_update` auf True gesetzt wird. Führt das System sobald es gestartet ist den Befehl `apt update` aus, der die Pakete aktualisiert. 