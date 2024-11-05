# Auftrag KN-08

## Einleitung

Der Auftrag in KN-08 ist keine Anleitung, die man befolgt und dann dokumentiert, sondern ein Auftrag einen **eigenen Auftrag zu erstellen**. Also das, in diesem Modul, Gelernte **praktisch umzusetzen**. In dieser Dokumentation werde ich genau zeigen *was ich gemacht hatte, wie ich es gemacht hatte und was für Schwierigkeiten und Probleme dabei auftauchten.* 

### Idee

Ich interessiere mich nicht nur für Plattformentwickler-spezifische Themen, sondern auch für Applikationsentwickler-Themen wie beispielsweise programmieren. Nicht all zu lange habe ich ein **Server-Client-Modell** mit Python programmiert. Es ist ein Chatroom-Server an dem sich Clients verbinden und mit **anderen Clients kommunizieren** können. Da der Schulstress zunahm konnte ich nicht viel daran weiterarbeiten. Jetzt hat es aber einen Zweck. Die Idee ist es, das **Server-Client-Modell in der AWS Cloud umzusetzen**. 

Um das Modell in der Cloud zu deployen muss es aber ein *wenig angepasst werden*. Momentan gibt es nur **einen** Server, der Anfragen verarbeiten kann. Was wenn es **mehrere** Server geben könnte. Somit könnte ein Auto-Scaler erstellt werden, der *mehrere Instanzen erstellt* und den Server darauf startet. Der traffic würde durch einen **Load Balancer** gleichmässig auf die Instanzen verteilt werden. Falls eine maximale Menge an Clients für einen Server erreicht wäre, würden einfach **noch mehr Server erstellt** werden. 

Diese Idee ist nicht zu einfach aber nicht zu schwierig für die Umsetzung und ist meiner Meinung nach perfekt für dieses Modul. 

## Vorbereitung

Der Hauptteil der Vorbereitung ist die **Programmierung vom Server**. Der Server muss so programmiert sein, dass *mehrere Server miteinander kommunizieren und Anfragen verarbeiten* können. Jeder Server muss von Clients erhaltene Anfragen an **alle Server broadcasten**, damit jeder **Client die Nachricht sehen** kann, *egal auf welchem Server* er verbunden ist. 

## Umsetzung in der Cloud
