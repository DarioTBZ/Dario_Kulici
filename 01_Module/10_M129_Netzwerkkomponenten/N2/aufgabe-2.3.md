# N2 Aufgabenstellung 2.3

### Vorgaben
- IP Range vom ISP: 34.112.98.0/24
- Drei unterschiedlich grosse Subnetze

### Netzwerk
Der ISP stellt ein /24er Netz zur Verfügung. Es sollen zwei Netzwerke erstellt werden. Das erste soll ein /26er und das zweite ein /28er sein. Das letzte Netzwerk soll ein Transfernetz sein mit der CIDR /30. 

| Subnetz ID | Netzwerk ID      | Verfügbare Adressen | Besetzte Adressen | Freie Adressen | Abteilung  |
| ---------- | ---------------- | ------------------- | ----------------- | -------------- | ---------- |
| 1          | 34.112.98.0/26   | 62                  | 3                 | 59             | Produktion |
| 2          | 34.112.98.64/28  | 14                  | 3                 | 11             | Verkauf    |
| 3          | 34.112.98.252/30 | 0                   | 4                 | 0              | Transfer   |

Das erste und zweite Subnetz hat 3 IP-Adressen. Dazu gehören der Router und zwei PCs. Im letzten Subnetz sind es zwei Router, die alle Adressen besetzen. 

### Excel Netzwerktabelle

Ich habe anhand vom [Bild im Auftrag](https://gitlab.com/ser-cal/m129-lb2/-/raw/main/N2/3/P2_3_subnetz-kreis_800.jpg) die Netzwerkkonfiguration auf Excel ausgefüllt.  

<img width=50% height=50% alt="Netzwerk1und2" src="">

### PC Konfiguration

#### PC in Subnetz 1

Das erste Subnetz ist ein /26er Netz. Da ist der Router die IP 34.112.98.1. 

<img width=50% height=50% alt="Subnetz1PC-ip" src="">

<img width=50% height=50% alt="Subnetz1PC-gateway" src="">

#### PC in Subnetz 2

Das zweite Subnetz ist ein /28er Netz. Da ist der Router die IP 34.112.98.65. 

<img width=50% height=50% alt="Subnetz2PC-ip" src="">

<img width=50% height=50% alt="Subnetz2PC-gateway" src="">

### Router Konfiguration

#### Router 1

| Interface       | IP-Adresse   | Subnetzmaske    |
| --------------- | ------------ | --------------- |
| FastEthernet0/0 | 34.112.98.1  | 255.255.255.192 |
| FastEthernet1/0 | 34.112.98.65 | 255.255.255.240 |

#### Router ISP

| Interface       | IP-Adresse    | Subnetzmaske    |
| --------------- | ------------- | --------------- |
| FastEthernet0/0 | 34.112.98.254 | 255.255.255.252 |

### Statische Routen

| Router     | Netzwerk      | Next Hop      | Subnetzmaske    |
| ---------- | ------------- | ------------- | --------------- |
| Router 1   | 0.0.0.0       | 0.0.0.0       | 0.0.0.0         |
| Router 1   | 34.112.98.252 | 34.112.98.254 | 255.255.255.252 |
| Router ISP | 0.0.0.0       | 34.112.98.253 | 255.255.255.252 |

Der **ISP Router** leitet **sämtlichen Traffic zum Router 1** weiter, da kein anderer Router angeschlossen ist als dieser. Router 1 hingegen leitet Traffic der für das Netzwerk 34.112.98.252 vorgesehen ist an den Router ISP weiter und den **Rest, also 0.0.0.0** an das andere Interface. 

### Testing

Ich habe wieder die ARP Tabellen der Router ausgefüllt, indem ich von überall hin und her PDUs gesendet habe. Danach konnte ich überall hin pingen und PDUs senden. 

<img width=50% height=50% alt="TestingPing" src="">

<img width=50% height=50% alt="TestingPDU" src="">

### Fragen
- Wieviele freie IP-Adressen gibt es in der Abteilung **Verkauf**
- Ist ein mögliches Wachstum der Firma berücksichtigt?
- Ist das Netzwerk-Design sinnvoll?
- Gibt es Verbesserungsvorschläge bzgl. Netzwerk-Design?
- Welche zusätzlichen Informationen wären nützlich, um für dieses Netzwerk-Design einen Optimierungsvorschlag auszuarbeiten?

### Antworten
- In der Abteilung Verkauf sind 11 IP-Adresse frei.
- Nein. Es sind sogar zu viele Geräte in der Abteilung Verkauf. Es sind 15 aber können maximal eigentlich 14 sein.
- Ja. Es ist grundsätzlich sinnvoll aufgebaut.
- Das Verkauf Netzwerk sollte kein /28er sein sondern vielleicht ein /26er. 
- Wie viel Personen pro Jahr in die Firma kommen. 