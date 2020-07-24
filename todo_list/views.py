from django.shortcuts import render
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):

	if request.method == 'POST':
		form = ListForm(request.POST or None)
		if form.is_valid():
			form.save()
			items = List.objects.all
			messages.success(request, ('Item Added Successfully!'))
			return render(request, 'home.html', {'items' : items})

	else:
		items = List.objects.all
		return render(request, 'home.html', {'items' : items})


def about(request):
	context = {'greeting' : 'Good Morning!', 'app' : 'To-Do List Application'}
	return render(request, 'about.html', context)

