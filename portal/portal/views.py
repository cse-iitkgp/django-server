from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render

def home(request):
	return render(request, "main.html")