#nohup gunicorn -b 0.0.0.0:8000 wsgi &
python manage.py runserver 0.0.0.0:8000 &
