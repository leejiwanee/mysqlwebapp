# mysqlwebapp
Django project for displaying data from MySQL database

# How to run

1. Login MySQL Database

2. Table name should be 'parameters' and table should have following requirements:
* id INT Not Null Auto Incremental
* name VARCHAR(200) Not Null
* values VARCHAR(45)
* allowed_values VARCHAR(200)
* modifiable BOOLEAN/TINY INT NOT NULL
* source VARCHAR(45) NOT NULL
* apply_type VARCHAR(45) NOT NULL
* data_type VARCHAR(45) NOT NULL
* description VARCHAR(200) NOT NULL

3. Modify settings for your database in setting.py
Ex) database name, user, password, host and port

4. Before running server, you should do 'pip install django-filter' and 'pip install django-db-logger'

5. Run django server 'python manage.py runserver'

6. If there is an error for LOGGING in setting.py, you should change the path of filename such as C:/.../webapp/webapp/logs/info.log
   Make sure that table name is same as db_table variable name in models.py Ex) 'parameters'


