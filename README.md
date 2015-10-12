# Setup

* Install [Vagrant](https://www.vagrantup.com/)
* ``cd`` into the folder containing the ``Vagrantfile``
* Run ``vagrant up``. This will download/run an Ubuntu virtual machine, and install all dependencies (as listed in ``boostrap.sh``) in it.
* Run ``vagrant ssh`` to ssh into the virtual machine. Note that all future commands should be run in the virtual machine. Also note that the directory containing the ``Vagrantfile`` on the host is synced to ``/vagrant`` in the virtual machine.
* Verify Django is installed with Python in your shell
```python
python
import django
print(django.get_version())
```
* Go to the ``appsite`` directory under the project directory and start up the barebone Django server
```bash
cd /vagrant/appsite/
python manage.py runserver
```
  Now you can access the barebone web server at ``http://127.0.0.1:8081/`` outside of the virtual machine.

## Setting up database
<small>https://docs.djangoproject.com/en/1.8/intro/tutorial01/</small>

In the project directory (the directory containing ``manage.py``), run:

```bash
python manage.py makemigrations bluehack
python manage.py sqlmigrate bluehack 0001 #optional; see the sql that will be run
python manage.py migrate
```

This will create the database schema defined by the models in ``models.py``.
