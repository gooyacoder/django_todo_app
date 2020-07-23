from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {})

def about(request):
	context = {'greeting' : 'Good Morning!', 'app' : 'To-Do List Application'}
	return render(request, 'about.html', context)

