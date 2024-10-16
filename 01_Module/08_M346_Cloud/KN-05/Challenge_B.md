# VPC mit je zwei Pulbic- und Private Subnets in zwei verschiedenen AZ erstellen

### Namensgebung

##### VPC
Name: M346-KUL-VPC
IPv4 CIDR Block: 10.0.0.0/16

##### Subnetze
Name: M346-KUL-**Public-1A**
AZ: us-east-1a
IPv4 CIDR Block: 10.0.1.0/24

Name: M346-KUL-**Public-1B**
AZ: us-east-1b
IPv4 CIDR Block: 10.0.2.0/24

Name: M346-KUL-**Private-1A**
AZ: us-east-1a
IPv4 CIDR Block: 10.0.3.0/24

Name: M346-KUL-**Private-1B**
AZ: us-east-1b
IPv4 CIDR Block: 10.0.4.0/24

##### Public route table
Name: M346-KUL-Public-RT

##### Private route table
Name: M346-KUL-Private-RT

VPC: M346-KUL-VPC

Subnet associations: Private-1A, Private-1B

##### Internet gateway
Name: M346-KUL-IGW

VPC: M346-KUL-VPC

##### NAT gateway
Name: M346-KUL-NAT-1A

### VPC Übersicht
Ich habe die VPC nach den Angaben erstellt. Standardmässig wird für jede AZ je ein private route table erstellt. Für die public subnets wurde nur ein route table erstellt, weshalb ich das für die privaten Subnetze auch so umsetzte. Im folgenden Bild erkennt man, dass nur noch ein route table für beide private subnets ersichtlich ist. 

Placeholder01

### Erklärung
Erst später bemerkte ich, dass man nur die VPC erstellen musste und die Subnetze manuell erstellen sollte. Ich habe die Subnetze schon bei der VPC Erstellung erstellt. Nachher musste ich nur noch die Subnetze umbenennen, den doppelten route table löschen, damit für public und private je ein route table existierte und den internet gateway + NAT gateway umbenennen. Der NAT Gateway war zwar nicht in der Übung, ist aber praktisch zu haben. 

Dadurch, dass die public subnets direkt ins Internet gelangen und die private subnets über den NAT ins Internet können, ist die Sicherheit auch für die private subnets garantiert. 

## Legende
- AZ = Availability Zone