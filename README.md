fchingalosite
=============
Library based website for consultancy institution.
It is python powered Django-cms website,
It aims to store, organize and download all references and reports for consultancy institution.
References are organized depending on their categories including Finance, Institution, Social and others.
Reports are organized depend on to whom the report have been sent.

How to install this site:
====================================
Install virtualenv on your machine and use it to maintain the site.
The following are couple of commands for operating under virtual env:

	#Install python virtualenv
	$ sudo apt-get install python-virtualenv
	
	#Create a virtual environment directory
	$ virtualenv /path/to/virtualenv_dir
	
	#Activating virtual environment(while you're in virtualenv_dir)
	$ source bin/activate
	
	#Deactivating virtual env
	$ deactivate

After creating and activating virtualenv, while inside virtualenv folder,
clone this site's source codes:
	
	$ git clone https://github.com/chingalo/fchingalosite.git

Inside fchingalosite directory, install project dependencies inside: deps.txt
	
	$ cd fchingalosite
	$ pip install -r deps.txt
Add database  configurations inside fchingalosite/settings.py, your
database configurations should look something similar to this:
	
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'HOST': 'localhost',
			'NAME': 'DATABASENAME',
			'USER': 'USERNAME',
			'PASSWORD': 'THESECRETPASSWORD',
			'PORT':'5432',
		}
	}
After configuration sync database( run command: python manage.py syncdb --all) and then run the server( run command: python manage.py runserver ).
Incase of any difficulties in configuration refer to [Django CMS Documentation](http://django-cms.readthedocs.org/en/2.2/getting_started/installation.html)
for more information.

