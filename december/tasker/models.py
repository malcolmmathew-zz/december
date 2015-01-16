from django.db import models
from django.utils import timezone
# Create your models here.

class Task(models.Model):
	task_name = models.CharField(max_length=25)
	task_description = models.CharField(max_length=250)
	deadline_date = models.DateTimeField('Deadline Date')

	def has_deadline_passed(self):
		return self.deadline_date <= timezone.now()

	def __str__(self):
		return self.task_name

