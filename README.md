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
python manage.py runserver 0.0.0.0:8000
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

## User Creation

* Go to ``http://127.0.0.1:8081/bluehack/`` and you will see fields to enter in order to register.

* Other than email and cellphone all other fields are required. You might be shown with a failed to register page if you fail the requirements.

* If you registered successfully you will be redirected to ``http://127.0.0.1:8081/bluehack/<username>/register`` and your account information will be retrieved from the database and displayed on this page.

* At the moment you can actually access any registered account information by going to this url: ``http://127.0.0.1:8081/bluehack/<username>/register`` For example the user ``testuser`` should already be created when I was testing it. You can look at the info of ``testuser`` by going
to ``http://127.0.0.1:8081/bluehack/testuser/register``.

I temporarily disabled crisis field in models for CrisisUser since it can't be null and I do not want to create one at this stage. The CrissiUser and built in User are attached/related with a <a href='https://docs.djangoproject.com/en/1.8/topics/db/examples/one_to_one/'>OneToOneField</a> relationship.

Key documentations:
* https://docs.djangoproject.com/en/1.8/topics/auth/default/
* https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-the-existing-user-model
* https://docs.djangoproject.com/en/1.8/topics/forms/

Key dirs (following official doc style):
* templates under appsite/bluehack/templates
* view at appsite/bluehack/views.py

.pyc files probably shouldn't be included in the commit but since Drini already did it last time and ``git add all`` is just so much easier might aswell.

