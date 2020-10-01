from django.shortcuts import render

#importing HttpResponse to provide the response for the end user
from django.http import HttpResponse


# Create your views here.
def display_data(request):
	data='<h1 style= "color:red">Hi Students .. welcome to learn Django by Sandesh</h1>'
	return HttpResponse(data)