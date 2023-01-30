from django.db import models

class CeleryLog(models.Model): # Logging using signals - core/signals.py
    task_id = models.CharField(blank=True, null=True, max_length=50)
    state = models.CharField(blank=True, null=True,  max_length=15)
    args = models.CharField(blank=True, null=True,  max_length=50)

    def __str__(self) :
     return self.task_id

class CeleryLog2(models.Model): # Logging using task events - core/celery_logger.py
    task_id = models.CharField(blank=True, null=True, max_length=50)
    state = models.CharField(blank=True, null=True,  max_length=15)
    args = models.CharField(blank=True, null=True,  max_length=50)

    def __str__(self) :
     return self.task_id