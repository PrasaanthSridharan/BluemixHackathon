# Get barebone Django server running

* Install Django with ``pip install Django``
* Verify Django is installed with Python in your shell

  ```python
  python
  import django
  print(django.get_version())
  ```

* Go to the ``appsite`` directory under the project directory and start up the barebone Django server
  ```bash
  cd BluemixHackathon/appsite/
  python manage.py runserver
  ```
  Now you can access the barebone web server at ``http://127.0.0.1:8000/``

  **Note: The port is 8000 not 8080 and depending on your working environment ``localhost`` might not work! Ofcourse all these can later be reconfigured**

## Setting up database
In the project directory (the directory containing ``manage.py``), run:

```bash
python manage.py makemigrations bluehack
python manage.py sqlmigrate bluehack 0001 #optional; see the sql that will be run
python manage.py migrate
```

This will create the database schema defined by the models in ``models.py``.

Database information: https://docs.djangoproject.com/en/1.8/topics/install/#database-installation

Basic database setup: https://docs.djangoproject.com/en/1.8/intro/tutorial01/
