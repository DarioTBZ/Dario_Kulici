
## Venv aktivieren

CMD öffnen **(Nicht Powershell)**

```
.\venv\scripts\activate.bat
```

Server starten. 

```
python manage.py runserver
```

Datenbank migrieren (Bei DB Änderungen)

```
python manage.py migrate
```