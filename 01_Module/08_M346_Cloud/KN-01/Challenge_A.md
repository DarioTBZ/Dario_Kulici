# Pricing und Instanzvergleich

Zu vergleichende Instanztypen:
- t2.micro
- m4.xlarge

### Leistungsvergleich

| Instance type | vCPUs | Architecture | Memory | Network performance |
| ------------- | ----- | ------------ | ------ | ------------------- |
| t2.micro      | 1     | i386, x86_64 | 1      | Low to Moderate     |
| m4.large      | 4     | x86_64       | 16     | High                |

Die Architektur ist hier nicht sehr bedeutend. Falls der Large Type eine ARM Architektur hätte, hätte man sagen können, dass man Strom spart. In diesem Fall ist es nicht wirklich ein Unterschied. 

### Preisvergleich

Die Preise variieren je nach Betriebssystem, weswegen der *Durchschnitt* der vier Systeme in der Tabelle steht. 

| Instance type | Price per hour | Price per day | Price per month |
| ------------- | -------------- | ------------- | --------------- |
| t2.micro      | 0.01635$       | 0.39$         | 11.77$          |
| m4.large      | 0.1552$        | 3.72$         | 111.74$         |

Mit der t2.micro Instanz würde man erst nach 61 Stunden auf **einen Dollar** kosten kommen. Mit dem m4.large hingegen schon nach 6.5 Stunden. Die m4.large Instanz kostet 10 Mal mehr als die t2.micro Instanz. 

### Use-Cases

##### t2.micro
- Einfacher Webserver
- Kleine Datenbank
- Testumgebung

##### m4.large
- Webserver & Anwendung
- grössere Datenbanken
- Software as a Service

### Scaling

##### Vertical Scaling
Hierbei wird die Instanz **einzeln** erhöht. Beispielsweise von einer t2.micro auf eine m4.large, wenn man mehr Leistung braucht. 
##### Horizontal Scaling
Beim Horizontal Scaling wird eine neue Instanz erstellt. Also laufen zwei parallel. 

Die Frage ist ob Horizontal Scaling oder Vertical Scaling besser passt. Es kommt ganz drauf an, was man mit den Instanzen macht. Bei einer Datenbankerweiterung macht ein Vertical Scaling mehr Sinn, weil die Datenbank auf einer Instanz läuft. Bei verteilten Systemen wie bspw. Webanwendungen macht ein Horizontal Scaling Sinn, weil es verschiedene Teile einer Gesamtanwendung gibt. 

## Quellen
- AWS Learner Lab