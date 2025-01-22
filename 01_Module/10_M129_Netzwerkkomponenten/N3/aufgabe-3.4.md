# N3 Aufgabenstellung 3.4

### Vorgaben 
- Netzwerkdesign erstellen
- Umgebung in Cisco Packet Tracer realisieren

### Netzwerkplanung

#### Netzgrössen

| Netz            | Benötigte Adressen          | Gewählte Netzgrösse | CIDR |
| --------------- | --------------------------- | ------------------- | ---- |
| Netz A (Global) | 30 PCs + 60 LTs + 7 DR = 97 | 128                 | 25   |
| Netz B  (Local) | 8 PCs + 7 LTs + 2 DR = 17   | 32                  | 27   |
| Netz Internet   | 2 RT = 2                    | 4                   | 30   |
| Transfer Netz   | 2 RT = 2                    | 4                   | 30   |

#### Netzadressen
| Netz            | Grösse | Netzadresse / Netzmaske | Dezimale Schreibweise der Netzmaske | Broadcastadresse |
| --------------- | ------ | ----------------------- | ----------------------------------- | ---------------- |
| Netz A (Global) | 128    | 178.19.22.0 /25         | 255.255.255.128                     | 178.19.22.127    |
| Netz B (Local)  | 32     | 178.19.22.128 /27       | 255.255.255.224                     | 178.19.22.159    |
| Netz Internet   | 4      | 178.19.22.252 /30       | 255.255.255.252                     | 178.19.22.255    |
| Transfer Netz   | 4      | 178.19.22.192 /30       | 255.255.255.252                     | 178.19.22.195    |

#### Diagramm

<img width=50% height=50% alt="Kuchendiagramm" src="https://github.com/user-attachments/assets/370bd3c3-610e-4640-93f5-b8e967620239">

Auf dem Bild sieht man, dass das Transfer Netzwerk zum ISP ganz am Ende des Netzwerks ist und das Transfer Netz von A nach B nach Netz B. 

**Transfernetz zu ISP**: 178.19.22.252

**Transfernetz A nach B**: 178.19.22.192


### Routerkonfiguration

#### Router Interfaces

| Router                 | Interfaceadresse | Interface |
| ---------------------- | ---------------- | --------- |
| Router A Netz A        | 178.19.22.1      | e0        |
| Router A Transfer Netz | 178.19.22.194    | s0        |
| Router A Internet      | 178.19.22.253    | s1        |
| Router B Netz B        | 178.19.22.129    | e0        |
| Router B Transfer Netz | 178.19.22.193    | s0        |

#### Routingtabelle Router A

| Destination Network   | Next Hop      | Metric | Interface (dieser Router) |
| --------------------- | ------------- | ------ | ------------------------- |
| (A) 178.19.22.0 /25   | 178.19.22.1   | 0      | e0                        |
| (B) 178.19.22.128 /27 | 178.19.22.193 | 1      | s0                        |
| (I) 178.19.22.252 /30 | 178.19.22.254 | 1      | s1                        |
| (T) 178.19.22.192 /30 | 178.19.22.193 | 1      | s0                        |
| (Default) 0.0.0.0 /0  | 178.19.22.254 | 1      | s1                        |

#### Routingtabelle Router B

| Destination Network   | Next Hop          | Metric | Interface (dieser Router) |
| --------------------- | ----------------- | ------ | ------------------------- |
| (A) 178.19.22.0 /25   | 178.19.22.194 /30 | 1      | s0                        |
| (B) 178.19.22.128 /27 | 178.19.22.129 /27 | 0      | e0                        |
| (I) 178.19.22.252 /30 | 178.19.22.194 /30 | 1      | s0                        |
| (T) 178.19.22.192 /30 | 178.19.22.194 /30 | 1      | s0                        |
| (Default) 0.0.0.0 /0  | 178.19.22.194 /30 | 1      | s0                        |

### Realisieren

Als erstes konfigurierte ich die Router zuerst mit den entsprechenden Interfaces. Zum Beispiel setzte ich die Router IP für das Netz A, also 178.19.22.1. 

<img width=50% height=50% alt="RealisierenNetzAConfig" src="https://github.com/user-attachments/assets/707ef054-295d-45ce-8f0d-c85a7b92aaf2">

Nachher setzte ich die Routen für alle Router. Beispielsweise die Route von Netz B zu Netz A. Das heisst Router B gibt alle Pakete die ins Netzwerk 178.19.22.0 müssen an die IP-Adresse von Router A über das Transfernetz. Der nächste Hop ist also 178.19.22.194. 

<img width=50% height=50% alt="RealisierenRTBRouten" src="https://github.com/user-attachments/assets/f2f65d34-6326-4422-8539-ceef0208222d">


### Testing

Ping von Netz A zu Netz B:

<img width=50% height=50% alt="TestingNetzAzuB" src="https://github.com/user-attachments/assets/c2887b78-d4ef-442a-bdf6-b2c95fbb593c">

Ping von Netz A zu ISP:

<img width=50% height=50% alt="TestingNetzAzuISP" src="https://github.com/user-attachments/assets/cef34d27-eaf3-4971-931a-8fd98fdb8082">

Ping von Netz B zu Netz A: 

<img width=50% height=50% alt="TestingNetzBzuA" src="https://github.com/user-attachments/assets/6fecaff2-aeb8-4557-99b2-143cfbb5adda">

Ping von Netz B zu ISP: 

<img width=50% height=50% alt="TestingNetzBzuISP" src="https://github.com/user-attachments/assets/246a27cc-8807-43d0-a014-25118f1a6cda">
