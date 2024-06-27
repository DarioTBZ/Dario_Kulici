# Datenkonsistenz / Datenintegrität
Die Datenkonsistenz / Datenintegrität wird gewährleistet durch diese Bedingungen: 
## Domänenintegrität / Bereichsintegrität
Attribute müssen gültige Werte haben. Beispielsweise kann in ein DATE-Attribut kein Text eingefügt werden, weil sonst das Attribut ungültig ist. 

## Enitätsintegrität 
Jeder Datensatz muss eindeutig definiert sein. Ein Beispiel ist der Primary Key. 

## Referentielle Integrität
Beziehungen zwischen Tabellen müssen synchronisiert sein. Wenn beispielsweise Fremdschlüssel existieren, die an keine Primary Keys gebunden sind, ist es eine Verletzung der referentiellen Integrität, da der Fremdschlüssel nirgendwo hinzeigt. 

### Grundregel
Fremdschlüssel müssen **immer** auf existierende Datensätze verweisen. Sonst für es zu ***Inkonsistenzen***. 


## Benutzerdefinierte Integrität
Sonderregeln, bei denen beispielsweise das Datum nicht vor 01.01.2000 liegen darf. 



# Aufgaben 
![](Pasted%20image%2020240326141323.png)

Die Operationen a, b und c sind zulässig. 