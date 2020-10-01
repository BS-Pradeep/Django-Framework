from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
# 
def bangalore_job(request):
	data='<h1>Bangalore Job Information</h1>'
	return HttpResponse(data)

def mysore_job(request):
	data='<h1>Mysore Job Information</h1>'
	return HttpResponse(data)

def mumbai_job(request):
	data='<h1>Mumbai Job Information</h1>'
	return HttpResponse(data)