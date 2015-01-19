from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django import forms
from forms import AddForm
from tasker.models import Task

# Create your views here.

def index(request):
	latest_task_list = Task.objects.order_by('-deadline_date')[:5]
	context = {'latest_task_list': latest_task_list}
	return render(request, 'tasker/index.html', context)

def detail(request, task_id):
	task = get_object_or_404(Task, pk = task_id)
	#if task.has_deadline_passed():
	#	has_deadline_passed = "Deadline has Passed!"
	#else:
	has_deadline_passed = str(task.deadline_date)
	return render(request, 'tasker/detail.html', {'task': task, 'has_deadline_passed': has_deadline_passed})

def edit(request, task_id):
	task = get_object_or_404(Task, pk = task_id)
	return render(request, 'tasker/edit.html', {'task': task})

def new(request):
	if request.method == 'POST':
		form = AddForm(request.POST)
		if form.is_valid():	
			#cd = form.cleaned_data
			newtask_name = form.cleaned_data['taskname']
			newtask_description = form.cleaned_data['taskdescription']
			#newdeadline_date = form.cleaned_data['deadlinedate']
			t = Task(task_name=newtask_name, task_description=newtask_description, deadline_date=timezone.now())
			t.save()
		return HttpResponseRedirect('/tasker/')
	else:
		form = AddForm()
	time = str(timezone.now())
	lol = time
	return render(request, 'tasker/new.html', {'form': form})

def delete(request):
	return render(request, 'tasker/index.html', context)