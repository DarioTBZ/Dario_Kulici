# Flow Control

## Checkpoint
- Wie wird der Programmfluss gesteuert?
- Welche Bedingungen gibt es in JAVA?
- Wie wird im Programm verzweigt?
- Wie wird ein Block wiederholt?
- Was ist eine Abstraktion? Wie funktioniert sie?

# Inhalt

Ein Java Programm besteht aus Blöcken mit Befehlen, die etwas ausführen. Es gibt die folgenden Bedingungen:
| Vergleich | Bsp.         | true, wenn der ...                                       |
| --------- | ------------ | -------------------------------------------------------- |
| =         | a == b       | Inhalt von a **gleich (identisch)** Inhalt von b ist (!) |
| ≠         | (a **!=** b) | Inhalt von a **nicht gleich** Inhalt von b ist           |
| <         | (a **<** b)  | Inhalt von a **kleiner** Inhalt von b ist                |
| ≤         | (a **<=** b) | Inhalt von a **kleiner oder gleich** Inhalt von b ist    |
| >         | (a **>** b)  | Inhalt von a **grösser** Inhalt von b ist                |
| ≥         | (a **>=** b) | Inhalt von a **grösser oder gleich** Inhalt von b ist    |

Note: Diese Tabelle ist vom Repository m319 kopiert worden.

### If- Schlaufen
Mit Bedingungen werden If- Schlaufen gebaut. 

Beispielsweise ist a = 1. Falls a = 2 ist, sollte eine Abfrage stattfinden. Der Befehl würde so aussehen: 
```
if (a == 2) {
InputInt("Dies ist eine Abfrage");
}
```

### Selektion
Programme werden nach Bedingungen verzweigt. Es gibt beispielsweise 2 Bedingungen. Wenn die erste erfüllt ist passiert etwas anderes als wenn die zweite Bedingung erfüllt ist. So kann das Programm nach belieben gestaltet werden. 

### Iteration
Wenn Bedingungen erfüllt sind, können Anweisungen mehrfach wiederholt werden. Dies wird mit While-Schleifen, For-Loops und break/continue Befehlen bezweckt. 

### Abstraktion 
Es hilft, wichtige Stücke Code in Funktionen zu tun. Das Programm zu unterteilen nennt man Abstraktion, damit man sieht was wo ist und welchem Zweck dient. 

# Lernziele
- I know what control flow means.
- How to control the program sequence.
- What conditions does JAVA have.
- What means of control flow does JAVA have.


- Flow Control ist der Kontrollfluss eines Programms. Man steuert den Ablauf eines Programms mit Abstraktionen, Iterationen und Selektionen. 
- 


https://gitlab.com/ch-tbz-it/Stud/m319/-/tree/main/N1-Flow_Control