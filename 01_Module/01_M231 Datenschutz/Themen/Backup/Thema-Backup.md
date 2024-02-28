# Was ist ein Backup?

Wortwörtlich übersetzt heisst **"Back up"** ***verstärken, zurückfahren oder unterstützen***. Es ist eine Sicherung von Daten, die man beschützen will, indem man sie, falls sie ausfallen, doppelt oder mehrfach sichert. Das Thema Backup ist gross, weshalb ich auf verschiedene Themen eingehen werde. 

## Datensicherungsziele - Wo werden Backups gespeichert?
Es ist wichtig zu entscheiden welche Daten man backupen will. Sei es eine Festplatte mit wichtigen Dateien oder die PCs von Mitarbeitern, die allesamt wichtige Daten sammeln, es muss entschieden werden, was man sichert. Nachdem man weiss, was man sichert, ist zu entscheiden wo man es speichert. Meist reichen Festplatten oder Server. Je nachdem wie schnell ein Backup gemacht sein sollte, kann man entscheiden, ob man eine SSD oder eine HDD nutzen will.

## 3 Sicherungsarten
Ein Backup kann verschieden sein. Eine Sicherung des ganzen Systems zu machen nennt man eine Vollsicherung, die letzten Änderungen zu sichern ist eine differenzielle Sicherung und wenn die letzten geänderten Daten gesichert werden, ist es eine inkrementelle Sicherung. 

### Vollsicherung
Benötigt viel Speicherplatz, dafür sind buchstäblich **ALLE** Daten gespeichert. Es ist vorteilhaft, dass alle Daten kopiert werden, da nichts fehlt. 

Nachteilhaft kann es sein, wenn das letzte Backup am Sonntag war und am Mittwoch das System ausfällt. Dann verliert man die Daten vom Montag bis Mittwoch und muss alles wieder neu erarbeiten. 

### Differenzielle Sicherung
Es sichert die letzten Änderungen im System. Speichert weniger Daten als das Vollbackup aber mehr als das inkrementelle Backup. Wenn am Sonntag ein Vollbackup erstellt wird, speichert das differenzielle Backup die Daten seit dem letzten Vollbackup. Das heisst am Dienstag speichert es die Daten vom Sonntag aus. 

Die Grösse der Backup Datei nimmt also mit der Zeit zu. Deswegen braucht das differenzielle Backup auch mehr Zeit, da die Datei immer grösser wird und neu kopiert wird. 

### Inkrementelle Sicherung 
Sichert nur die letzten Änderungen seit dem letzten Backup. Wenn am Sontag ein Vollbackup gemacht wird speichert das inkrementelle Backup die Daten am Montag vom Sonntag aus. Am Dienstag speichert es die Daten vom Montag aus. Das inkrementelle Backup ist am schnellsten von allen, da es auch am wenigsten Daten speichert. 

Der Nachteil an diesem Backup Typ ist, dass wenn die Daten wiederhergestellt werden müssen, alle Backups vom letzten Vollbackup benötigt werden. Wenn der Absturz am Donnerstag ist, werden die Backups vom Montag bis Mittwoch gebraucht. Dadurch ist der Prozess komplexer. 

*Für die inkrementelle und differenzielle Sicherung wird immer ein Vollbackup benötigt.*

## Block-Level vs. File-Level Backup
Das Block- und File-level Backup sind Features vom inkrementellen Backup. Das File Level Backup scannt das System nach Dateien, die verändert wurden und kopiert die ganzen Dateien mit den Änderungen. Das ist anspruchsvoller und braucht mehr Speicherplatz. Dafür ist es simple und es kann ausgewählt werden, welche Dateien oder welcher Dateityp gesichert wird. 

Das Block-Level Backup schaut nach, welche Teile von Dateien verändert wurden und sichert diese ins Backup. Vorteile sind, dass es schneller ist und weniger Speicherplatz braucht. Die dunkle Seite vom Block-Level Backup ist, dass die Wiederherstellung der Daten länger geht, da alle Teile der Dateien wieder zusammengefügt werden müssen. Wenn ein Teil einer Datei fehlt, kann sie nicht wiederhergestellt werden. 

## Hot und Cold Backup
Unter einem Hot Backup versteht man ein Backup, das während dem Benutzen von Dateien gemacht wird. Ein Cold Backup findet statt, wenn die Dateien **nicht** gebraucht werden bzw. das System *"kalt"* ist, also heruntergefahren wurde. 

Datenbanken haben meistens *dynamische Backup Methoden*, in diesem Fall **Hot Backups**, da man während dem Arbeiten Backups durchführen kann. Bei Cold Backups werden *meistens Vollsicherungen* auf ein sekundäres Laufwerk gemacht. Dabei muss **das ganze** System heruntergefahren werden und es können keine Änderungen an Dateien vorgenommen werden. 

## Datensicherungsstrategien
Unter einer **Datensicherungsstrategie** versteht man eine *Herangehensweise wie man bestimmte Daten schützen* möchte. Wenn eine kleine Firma **1 TB** Daten besitzt, die auf keinen Fall gelöscht werden dürfen, weil bspw. sonst Transaktionsdaten verloren gehen, muss eine Datensicherungsstrategie her. Dann wird entschieden ob man *bswp. am Sonntag ein Vollbackup und während der Woche inkrementelle Backups durchführt*. Es sollte auch regelmässig überprüft werden, **ob die Wiederherstellung funktioniert**. Falls es Fehler gibt, müssen diese behoben werden, um die Sicherheit der Daten zu bestätigen. 

# Quellen

### Datensicherungsziele - Wo werden Backups gespeichert
- https://brekom.de/ratgeber-it-sicherheit/datensicherung/#:~:text=Ziel%20der%20Datensicherung%20ist%20es,dies%20Datenwiederherstellung%20oder%20auch%20Restore.

### 3 Sicherungsarten
- https://aws.amazon.com/de/compare/the-difference-between-incremental-differential-and-other-backups/#:~:text=Inkrementelle%20Backups%20ben%C3%B6tigen%20weniger%20Speicherplatz,indem%20der%20Speicherplatz%20beeintr%C3%A4chtigt%20wird.
- https://www.langmeier-software.com/de/seiten/kmu-datensicherung/inkrementelles-backup#:~:text=Wird%20inkrementell%20ein%20Backup%20durchgef%C3%BChrt,Betriebssystems%20einmal%20vollst%C3%A4ndig%20gesichert%20werden.
- https://www.ahd.de/differentielles-backup-sichern-sie-daten-effizienter/#:~:text=Ein%20Beispiel%3A%20Am%20Montag%20wurde,die%20differentielle%20Sicherung%20vom%20Donnerstagabend.

### Block-Level vs. File-Level Backup
- https://www.backblaze.com/blog/whats-the-diff-file-level-vs-block-level-incremental-backups/

### Hot und Cold Backup
https://de.minitool.com/datensicherung/hot-backup-verglichen-mit-cold-backup.html

### Datensicherungsstrategien
- https://www.zmanda.com/de/Blog/effektive-Datensicherungsstrategie/#:~:text=eine%20Datensicherungsstrategie%20ist.-,Was%20ist%20eine%20Datensicherungsstrategie%3F,oft%20die%20Sicherung%20stattfinden%20soll.