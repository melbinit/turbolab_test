# https://docs.celeryq.dev/en/stable/userguide/monitoring.html

import os # https://docs.djangoproject.com/en/4.1/topics/settings/#calling-django-setup-is-required-for-standalone-django-usage
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tlabs_task.settings")
django.setup()

from tlabs_task.celery  import app
from core.models import CeleryLog2

def my_monitor(app):
    state = app.events.State()
    def announce_received_tasks(event):
        state.event(event)
        try:
            task = state.tasks.get(event['uuid'])
            args = eval(task.info().get('args'))  
            args_str = args[0] + "," + str(args[1])
            CeleryLog2.objects.create(task_id = task.uuid, state = "RECEIVED", args = args_str)
            print("Received :::", task.uuid)
        except Exception as e:
            print(e)

    def announce_started_tasks(event):
        state.event(event)
        try:
            task = state.tasks.get(event['uuid'])
            task_obj = CeleryLog2.objects.get(task_id = task.uuid)
            task_obj.state = "RUNNING"
            task_obj.save()
            print("Running :::", task.uuid)
        except Exception as e:
            print(e)
    
    def announce_succeeded_tasks(event):
        state.event(event)
        try:
            task = state.tasks.get(event['uuid'])
            task_obj = CeleryLog2.objects.get(task_id = task.uuid)
            task_obj.state = "SUCCESS"
            task_obj.save()
            print("Success :::", task.id)
        except Exception as e:
            print(e)

    def announce_failed_tasks(event):
        state.event(event)
        try:
            task = state.tasks.get(event['uuid'])
            task_obj = CeleryLog2.objects.get(task_id = task.uuid)
            task_obj.state = "FAILED"
            task_obj.save()
            print("Failed :::", task.uuid)
        except Exception as e:
            print(e)

    with app.connection() as connection:
        recv = app.events.Receiver(connection, handlers={
                'task-received': announce_received_tasks,
                'task-started': announce_started_tasks,
                'task-succeeded': announce_succeeded_tasks,
                'task-failed': announce_failed_tasks,
        })
        recv.capture(limit=None, timeout=None, wakeup=True)

if __name__ == '__main__':
    my_monitor(app)