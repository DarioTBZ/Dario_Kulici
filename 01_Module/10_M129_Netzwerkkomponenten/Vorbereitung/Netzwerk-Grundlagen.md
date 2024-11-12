# Netzwerk-Grundlagen

### OSI Modell

Layers sind Schichten, auf denen sämtliche Protokolle, Programme usw. basiert. Sie sind die Reihenfolge, in denen Prozesse und Abläufe funktionieren. Ein Computer sendet Pakete über jede einzelne Layer. 

#### Layer 1
Das ist die Transport-Layer. Hier werden Daten von A nach B übermittelt. Typische Protokolle sind z.B, TCP und UDP. TCP wird heutzutage häufiger verwendet, weil es Pakete sehr zuverlässig sendet. UDP sendet die Pakete einfach so, ohne zu überprüfen ob der Empfänger die Pakete erhalten hat. Deswegen ist **UDP schneller aber unzuverlässiger** und **TCP langsamer aber zuverlässig**. 