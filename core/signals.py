from celery.signals import task_prerun, task_postrun, task_unknown
from core.models import CeleryLog

# https://docs.celeryq.dev/en/stable/userguide/signals.html#signals

# logging
@task_prerun.connect()
def task_prerun_notifier(task_id=None, args=None, **kwargs):
    state = "RUNNING"
    CeleryLog.objects.create(task_id = task_id, state = state, args= str(args))

@task_postrun.connect()
def task_postrun_notifier(task_id=None, state=None, **kwargs):
    try :
        task = CeleryLog.objects.get(task_id = task_id)
        task.state = state
        task.save()
    except Exception as e:
        print(e)

@task_unknown.connect()
def task_unknown_notifier(task_id=None, **kwargs):
    try:
        state = "PENDING"
        task = CeleryLog.objects.get(task_id = task_id)
        task.state = state
        task.save()
    except Exception as e:
        print(e)
