**Logging using Celery signals and Task events**\
*They are logged into 2 seperate models. Celerylog and CeleryLog2 respectively.*


virtualenv venv\
venv/Scripts/activate (windows)\
pip install -r requirements.txt

```python
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Run redis server

Run celery :
```python
  celery -A tlabs_task worker --pool=solo -l info --task-events
```

Run core/celery_logger.py:
```python
  python -m core.celery_logger
```

python manage.py shell
```python
from core.task import generate_file
generate_file.delay("test_filename.csv", 40)
```
Or, for csv using pandas
```python
from core.task import generate_file2
generate_file2.delay("test_filename.csv", 50)
```

http://127.0.0.1:8000/admin

