# Arten von Verschlüsselungen

Um Daten zu verschlüsseln, damit sie sicher übertragen werden können, gibt es 2 Arten von Verschlüsselungen. Die sichere Variante ist 
die symmetrische Verschlüsselung. Leider ist es aufwendig, sie zu entschlüsseln. Bei der asymmetrischen Verschlüsselung werden die Daten 
viel einfacher verschlüsselt und sind daher auch einfacher zu entschlüsseln. 

## Asymmetrische Verschlüsselung 
Es gibt einen öffentlichen und privaten Schlüssel. Wenn **Host A** eine Datei verschlüsselt und sie zu **Host B** senden möchte, kann er die Datei bspw. 
mit dem *öffentlichen Schüssel* **von Host B** verschlüsseln. **Nur** Host B kann die Datei mit seinem **privaten Schlüssel** entschlüsseln. 

## Symmetrische Verschlüsselung
Hierbei gibt es nur **einen** Schlüssel für die Verschlüsslung und die Entschlüsselung. Eine Nachricht wird bspw. mit *Schlüssel F* verschlüsselt. Die Person, 
die die Nachricht entschlüsseln will, benötigt den **selben Schlüssel**. Das heisst der Schlüssel **muss** für die Sicherheit der Nachricht *geheim* 
übermittelt werden. 


# Unterthemen
- [Cäsar Verschlüsselung](CäsarVerschlüsselung.md)
- [Authentifizierung vs Autorisierung](AuthentifizierungvsAutorisierung.md)