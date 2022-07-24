1.Clone the git repo using this -  git clone 
2.Run pip install -r requirements.txt
3.configure settings.py file for postgres database,
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'automation_project00',
       'USER': 'your_postgres_username',
       'PASSWORD': 'your_postgres_password',

   }
}
4.create a database  in your postgres,you can use pgadmin4 this,rename the database as "automation_project00"
5.Run python manage.py makemigrations
6.Run python manage.py migrate
