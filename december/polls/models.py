from django.db import models

# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=250)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=250)
	votes = models.IntegerField(default=0)

class TestClass(models.Model):
	test = models.CharField(max_length=2)

#ADDED A COMMENT