Librairies utilisées :

Depuis la console (windows) ou terminal (linux/macOS)

pip install django
pip install pillow

Quick start
-----------
If python many Python versions are installed you have to use the latest version in your commands : replace python by python3 or pip by pip3

1. From the Terminal run 'pip3 install Django==2.0.6'

2. Use the cd command to go to your project folder.

3. Run 'django-admin startproject IGIPOP' if you want to create a new project. To add an application (blog for instance) : use the command 'python manage.py startapp blog'

3. Run `python manage.py makemigrations` and then `python manage.py migrate` to create the models (BDD).

4. Start the development server : 'python3 manage.py runserver' and visit http://127.0.0.1:8000/admin/

5. Visit http://127.0.0.1:8000/ to access the website