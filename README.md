# Get barebone Django server running

* Install Django with ``pip install Django``
* Verify Django is installed with Python in your shell
  ```
  Python
  >>>import django
  >>> print(django.get_version())
  1.8.5
  ```
* Go to the ``appsite`` directory under the project directory and start up the barebone Django server
  ```
  cd BluemixHackathon/appsite/
  python manage.py runserver
  ```
  Now you can access the barebone web server at ``http://127.0.0.1:8000/``
  
  **Note: The port is 8000 not 8080 and depending on your working environment ``localhost`` might not work! Ofcourse all these can later be reconfigured**

### Next step: Database installation and configuration
Database information: https://docs.djangoproject.com/en/1.8/topics/install/#database-installation

Basic database setup: https://docs.djangoproject.com/en/1.8/intro/tutorial01/ 
