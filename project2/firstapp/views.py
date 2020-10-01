from django.shortcuts import render

from django.http import HttpResponse
import datetime
# Create your views here.

#Function Based View
def welcome_clients(request):
	date=datetime.datetime.now()
	#the type of date is Date Object
	
	msg1='<h1>Welcome clients</h1>'
	msg2=msg1+'<h1>The current server time is :' + str(date) +'</h1>'

	return HttpResponse(msg2)
