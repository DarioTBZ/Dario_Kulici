
# N3 Aufgabenstellung 3.5


### Vorgaben 
- Netzwerkdesign erstellen
- Umgebung in Cisco Packet Tracer realisieren

### Netzwerkplanung


#### Netzgrössen

| Netz   | Benötigte Adressen           | Gewählte Netzgrösse | CIDR |
| ------ | ---------------------------- | ------------------- | ---- |
| Netz T | 2 RT = 2                     | 4                   | 30   |
| Netz I | 2 RT = 2                     | 4                   | 30   |
| Netz A | 23 PCs + 20 LTs + 7 DR = 50  | 64                  | 26   |
| Netz B | 65 PCs + 55 LTs + 7 DR = 127 | 256                 | 24   |

#### Netzadressen
| Netz   | Grösse | Netzadresse / Netzmaske | Dezimale Schreibweise der Netzmaske | Broadcastadresse |
| ------ | ------ | ----------------------- | ----------------------------------- | ---------------- |
| Netz T | 4      | 192.168.100.252         | 255.255.255.252                     | 192.168.100.255  |
| Netz I | 4      | 192.168.100.248         | 255.255.255.252                     | 192.168.100.251  |
| Netz A | 64     | 192.168.100.0           | 255.255.255.192                     | 192.168.100.63   |
| Netz B | 255    | 192.168.101.0           | 255.255.255.0                       | 192.168.101.255  |

### Diagramm 

<img width=50% height=50% alt="Kuchendiagramm-3.5" src="">

Netz A hat 50 Geräte und ein Netz mit 62 Adressen. Bei **Netz B ist das Problem**, dass ein /25er **Netz zu klein ist**. Deswegen muss ein **grösseres** genommen werden, also ein /24er. Dadurch, dass aber auf dem **ersten Kreis** kein Platz mehr ist, ist Netz B einfach auf dem **zweiten Kreis**. Die Transfer Netze sind am Ende des ersten Kreises, da sonst kein Platz mehr da ist. 

### Router Konfiguration

#### Router Interfaces

| Router           | Interfaceadresse | Interface |
| ---------------- | ---------------- | --------- |
| Router A Netz I  | 95.2.50.102      | fa2       |
| Router A Netz A  | 192.168.100.1    | fa0       |
| Router A Netz T  | 192.168.100.253  | fa1       |
| Router B Netz B  | 192.168.101.1    | fa0       |
| Router B  Netz T | 192.168.100.254  | fa1       |

#### Routingtabelle Router A

| Destination Network     | Next Hop        | Metric | Interface (dieser Router) |
| ----------------------- | --------------- | ------ | ------------------------- |
| (B) 192.168.101.0 /24   | 192.168.100.254 | 2      | fa1                       |
| (A) 192.168.100.0 /26   | 192.168.100.1   | 0      | fa0                       |
| (T) 192.168.100.252 /30 | 192.168.100.253 | 0      | fa1                       |
| (I) 95.2.50.100 /30     | 95.2.50.101     | 1      | fa2                       |
| (Default) 0.0.0.0 /0    | 95.2.50.101     | 1      | fa2                       |

#### Routingtabelle Router B

| Destination Network     | Next Hop        | Metric | Interface (dieser Router) |
| ----------------------- | --------------- | ------ | ------------------------- |
| (B) 192.168.101.0 /24   | 192.168.101.1   | 0      | fa0                       |
| (T) 192.168.100.252 /30 | 192.168.100.253 | 0      | fa1                       |
| (Default) 0.0.0.0 /0    | 192.168.100.253 | 1      | fa1                       |

### Realisieren

Zuerst konfigurierte ich alle **Interfaces der Router**. Bei Router A sind es beispielsweise **3 Interfaces** zum ISP, zum Transfer Netz und zum eigenen Netzwerk (Netz A). 

Danach definierte ich die Routen von allen Router, damit die Pakete korrekt gerouted werden. Auf Router B sind zwei Routen definiert. Eine zeigt zum Transfernetz (192.168.100.252) und die andere ist die Default Route, die auch zum Transfernetz zeigt. 

### Testing

Ping von Netz A zu Netz B:

<img width=50% height=50% alt="TestingNetzAzuB" src="">

Ping von Netz A zu ISP:

<img width=50% height=50% alt="TestingNetzAzuISP" src="">

Ping von Netz B zu Netz A: 

<img width=50% height=50% alt="TestingNetzBzuA" src="">

Ping von Netz B zu ISP: 

<img width=50% height=50% alt="TestingNetzBzuISP" src="https">

