from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_desc = models.TextField(max_length=200)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.task_name