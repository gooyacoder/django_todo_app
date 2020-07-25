from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):

	if request.method == 'POST':
		form = ListForm(request.POST or None)
		if form.is_valid():
			form.save()
			items = List.objects.all
			messages.success(request, ('Item is added successfully!'))
			return render(request, 'home.html', {'items' : items})

	else:
		items = List.objects.all
		return render(request, 'home.html', {'items' : items})


def about(request):
	context = {'greeting' : 'Good Morning!', 'app' : 'To-Do List Application'}
	return render(request, 'about.html', context)


def delete(request, id):
	item = List.objects.get(pk=id)
	item.delete()
	messages.success(request, ('Item is deleted successfully!'))
	return redirect('home')

def cross_off(request, id):
	item = List.objects.get(pk=id)
	item.completed = True
	item.save()
	return redirect('home')

def uncross(request, id):
	item = List.objects.get(pk=id)
	item.completed = False
	item.save()
	return redirect('home')
