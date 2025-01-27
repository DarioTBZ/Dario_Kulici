
## Venv aktivieren

#### Windows

CMD öffnen **(Nicht Powershell)**

```
.\venv\scripts\activate.bat
```
#### Mac

```
source venv/bin/activate
```

## Venv installieren und aufsetzen


Venv Ordner erstellen. 

```
python -m venv venv
```

Venv aktivieren. 

**Dann erst** nächsten Befehl ausführen. 

#### Windows
```
pip install -r requirements.txt
```
#### Mac
```
pip3 install -r requirements.txt
```


## Server starten

```
python manage.py runserver
```

Datenbank migrieren (Bei DB Änderungen)

```
python manage.py migrate
```

Statische Dateien sammeln

```
python manage.py collectstatic
```