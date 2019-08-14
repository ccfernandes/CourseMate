from django.shortcuts import render #render is for templates
from django.http import HttpResponse 
from .models import Tutorial

import datetime

#just regular python functions with user requests 
	#login/logout 
	#play video?

# Create your views here.
def homepage(request): #for any view, always pass request 
    return render(request=request, #so u can reference things inside your template to do with the user
                    template_name="main/home.html", #tells django location of template to be rendered
                    context={"tutorials": Tutorial.objects.all} #referrencing all the tutorials in the template?
                )

def about(request):
	return render(request=request, #so u can reference things inside your template to do with the user
                    template_name="main/AboutUs.html")

def login(request):
	now=datetime.datetime.now()
	return render(request=request, template_name="main/login.html", context={'datetime_now':now})

def current_date_time(request):
	now=datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)
