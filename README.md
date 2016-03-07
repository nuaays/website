# author: wanghe 

# django-oauth-toolkit-example  集成进了我们的官网系统  

# INSTALL && RUN

- virtualenv env 
- source env/bin/active 
- pip install -r requirements.txt
- python manage.py syncdb
- python manage.py migrate website
- python manage.py migrate example 
- python manage.py migrate oauth_provider
- python manage.py runserver 

- website: http://localhost:8000
- register app: http://localhost:8000/o/applications


