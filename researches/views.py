from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def research(request):
	context = {}

	return render(request, 'researches/hello.html ', context)


def get_login(request):
	context = {}
	return render(request, 'researches/login.html ', context)



