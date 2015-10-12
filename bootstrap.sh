apt-get update

# PostgresSql
apt-get install -y postgresql postgresql-contrib
apt-get install -y python-psycopg2
sudo -i -u postgres psql -f /vagrant/psqlBootstrap.sql

# Django
apt-get install -y python-pip
pip install django
