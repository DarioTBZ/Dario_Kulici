
## Speicherdienste Vergleich

| Persistenz | Geschwindigkeit | Sicherheit    | Standorte                                                   | Use-case                                       | Andwendungsbeispiel              |
| ---------- | --------------- | ------------- | ----------------------------------------------------------- | ---------------------------------------------- | -------------------------------- |
| Ja         | Eher langsam    | Verschlüsselt | Weltweit verfügbar                                          | Objektspeicherung von unveränderten Daten      | Bilder oder Videos               |
| Ja         | Schnell         | Verschlüsselt | Bestimmte Regionen (Availability Zone)                      | Blockspeicherung, Datenbanken, Betriebssysteme | Datenbankhosting                 |
| Ja         | Mittel          | Verschlüsselt | Bestimmte Regionen aber gleichzeitiger Zugriff ist möglich. | Netzwerkdateisystem für EC2 Instanzen          | Teilen von Konfigurationsdateien |

Zusammenfassend kann man sagen, dass ich der S3 Bucket für grosse Dateien lohnt, die sich selten ändern, der EBS ideal für hohe Leistungen ist und EFS top für gleichzeitigen Zugriff von mehreren Instanzen ist. 

## Quellen 
- [ChatGPT](https://chatgpt.com/share/66ffd016-b710-8010-be54-3cd123da895d) 