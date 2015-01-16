from django import forms
from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class AddForm(forms.Form):
	taskname = forms.CharField(label="Task Name:", max_length=25)
	taskdescription = forms.CharField(label="Task Description:", max_length=250)
	deadlinedate = forms.DateField(widget=DateInput(), label="Deadline Date:")
