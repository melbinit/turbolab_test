virtualenv venv
venv/Scripts/activate (windows)
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Run redis server

Run celery :
  celery -A tlabs_task worker --pool=solo -l info
  
python manage.py shell
>> from core.task import generate_file
>> generate_file.delay("abcd.csv", 40)

http://127.0.0.1:8000/admin