from django.shortcuts import render

from django.http import HttpResponse
import datetime
# Create your views here.

#Function Based View
def welcome_clients(request):
	date=datetime.datetime.now()
	hour=int(datetime.datetime.now().hour)
	msg='<h1>Hi Students Good'
	if hour>0 and hour<12:
		msg=msg+'<h1>Morning</h1>'
	elif hour>12 and hour<16:
		msg=msg+'<h1>Afternoon</h1>'
	elif hour>16 and hour<21:
		msg+='<h1>Evening</h1>'
	else:
		msg=msg+'<h1>Night</h1>'
	msg=msg+'</h1><hr>'

	msg=msg+'<h1>The server time is : '+str(date)+'</h1>'
	
	return HttpResponse(msg)
