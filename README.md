# Youtube Api with Dashboard

##Steps

1. Clone the project
2. cd djangorest
3. Run `python manage.py runserver` in terminal
4. Run `celery -A djangorest worker -l info && celery -A djangorest beat -l info` in other terminal


Url :

1. Api Can be accessed Here:
http://127.0.0.1:8000/api/videos/?page=11&query=Google

2. Dashboard Can be accessed Here:
http://127.0.0.1:8000/
