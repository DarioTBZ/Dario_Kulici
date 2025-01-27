# N3 Aufgabenstellung 3.6

### Vorgaben
- Netzwerkdesign erstellen
- Umgebung in Cisco Packet Tracer realisieren


### Netzwerkplanung 


#### Netzgrössen

| Netz    | Benötigte Adressen              | Gewählte Netzgrösse | CIDR |
| ------- | ------------------------------- | ------------------- | ---- |
| Netz A  | 25 PCs + 50 LTs + 5 DR = 80     | 128                 | 25   |
| Netz B  | 290 PCs + 510 LTs + 20 DR = 820 | 1024                | 22   |
| Netz C  | 120 PCs + 200 LTs + 10 DR = 330 | 512                 | 23   |
| Netz T1 | 2 RT = 2                        | 4                   | 30   |
| Netz T2 | 2 RT = 2                        | 4                   | 30   |
| Netz I  | 2 RT = 2                        | 4                   | 30   |

#### Netzadressen


| Netz    | Grösse | Netzadresse / Netzmaske | Dezimale Schreibweise der Netzmaske | Broadcastadresse    |
| ------- | ------ | ----------------------- | ----------------------------------- | ------------------- |
| Netz A  | 128    | 135.233.178.0 /25       | 255.255.255.128                     | 135.233.178.127     |
| Netz B  | 1024   | 135.233.180.0 /22       | 255.255.252.0                       | 135.233.183.255     |
| Netz C  | 512    | 135.233.176.0 /23       | 255.255.254.0                       | 135.233.177.255     |
| Netz T1 | 4      | 135.233.178.248 /30     | 255.255.255.252                     | 135.233.178.253 /30 |
| Netz T2 | 4      | 135.233.178.244 /30     | 255.255.255.252                     | 135.233.178.247 /30 |
| Netz I  | 4      | 135.233.178.252 /30     | 255.255.255.252                     | 135.233.178.178.255 |


### Diagramm

<img width=50% height=50% alt="Kuchendiagramm_3.6" src="https://github.com/user-attachments/assets/19a2da22-0f4d-476b-9635-761d37e8bf6b">

Netz C ist ganz am Anfang des Netzwerks, dann folgen Netz A, I, T1, T2 und zum Schluss ist Netzwerk B mit 1024 IP-Adressen. Die Aufteilung wo die Netzwerke sind hätte man anders machen können. Ich habe **es so gelöst**, dass **Netz B ganz am Schluss** ist und der Rest **am Anfang vom Netzwerk**. 

### Router Konfiguration

#### Router Interfaces

| Router            | Interfaceadresse | Interface |
| ----------------- | ---------------- | --------- |
| Router A Netz I   | 135.233.178.253  | fa2       |
| Router A Netz A   | 135.233.178.1    | fa0       |
| Router A Netz T1  | 135.233.178.249  | fa1       |
| Router B Netz T1  | 135.233.178.250  | fa1       |
| Router B  Netz T2 | 135.233.178.245  | fa2       |
| Router B Netz B   | 135.233.180.1    | fa0       |
| Router C Netz T2  | 135.233.178.246  | fa1       |
| Router C Netz C   | 135.233.176.1    | fa0       |

#### Routingtabelle Router A

| Destination Network  | Next Hop        | Metric | Interface (dieser Router) |
| -------------------- | --------------- | ------ | ------------------------- |
| (I) 135.233.178.252  | 135.233.178.254 | 0      | fa2                       |
| (A) 135.233.178.1    | 135.233.178.1   | 0      | fa0                       |
| (T1) 135.233.178.248 | 135.233.178.250 | 0      | fa1                       |
| (T2) 135.233.178.244 | 135.233.178.250 | 1      | fa1                       |
| (B) 135.233.180.0    | 135.233.178.250 | 1      | fa1                       |
| (C) 135.233.176.0    | 135.233.178.250 | 2      | fa1                       |
| (Default) 0.0.0.0    | 135.233.178.254 | 0      | fa2                       |

#### Routingtabelle Router B

| Destination Network  | Next Hop        | Metric | Interface (dieser Router) |
| -------------------- | --------------- | ------ | ------------------------- |
| (T1) 135.233.178.248 | 135.233.178.249 | 0      | fa1                       |
| (T2) 135.233.178.244 | 135.233.178.246 | 0      | fa2                       |
| (B) 135.233.180.0    | 135.233.180.1   | 0      | fa0                       |
| (C) 135.233.176.0    | 135.233.178.246 | 0      | fa2                       |
| (Default) 0.0.0.0    | 135.233.178.249 | 0      | fa1                       |

#### Routingtabelle Router C

| Destination Network  | Next Hop        | Metric | Interface (dieser Router) |
| -------------------- | --------------- | ------ | ------------------------- |
| (T2) 135.233.178.244 | 135.233.178.245 | 0      | fa1                       |
| (C) 135.233.176.1    | 135.233.176.1   | 0      | fa0                       |
| (Default) 0.0.0.0    | 135.233.178.245 | 0      | fa1                       |

### Exceltabellen

<img width=50% height=50% alt="ExcelNetzwerkB" src="https://github.com/user-attachments/assets/5748cb4f-2419-4e1c-a660-4d942e6a4a52">

<img width=50% height=50% alt="ExcelNetzwerkC" src="https://github.com/user-attachments/assets/7d58e2c7-b62b-42cc-92f2-c5a1e8fa988f">

Auf diesen Bildern sieht man die Excel Konfigurationen der Netzwerke B und C. 

### Konfiguration PCs

| ID  | Name             | IP-Adresse    | CIDR |
| --- | ---------------- | ------------- | ---- |
| 1   | PC-1822          | 135.233.178.2 | 25   |
| 2   | LT-1823          | 135.233.178.3 | 25   |
| 3   | PC2              | 135.233.180.2 | 22   |
| 4   | LT-1763          | 135.233.180.3 | 22   |
| 5   | PC-1802          | 135.233.176.2 | 23   |
| 6   | Laptop-PTLT-1803 | 135.233.176.3 | 23   |

### Subnetze

| Netz ID | Netzwerk ID     | Verfügbare Adressen | Besetzte Adressen | Freie Adressen |
| ------- | --------------- | ------------------- | ----------------- | -------------- |
| A       | 135.233.178.0   | 126                 | 3                 | 123            |
| B       | 135.233.180.0   | 1022                | 3                 | 1019           |
| C       | 135.233.176.0   | 510                 | 3                 | 507            |
| I       | 135.233.178.252 | 2                   | 2                 | 0              |
| T1      | 135.233.178.248 | 2                   | 2                 | 0              |
| T2      | 135.233.178.244 | 2                   | 2                 | 0              |

### Testing

Ping von Netz A zu Netz B und C:

<img width=50% height=50% alt="TestingPingvonAzuBC" src="https://github.com/user-attachments/assets/5a5ff939-076c-4eba-bc94-5a99c1738836">

Ping von Netz B zu Internet:

<img width=50% height=50% alt="TestingPingvonBzuInternet" src="https://github.com/user-attachments/assets/3efd9f17-1c09-4f2c-ab6c-1e92d29d304d">

