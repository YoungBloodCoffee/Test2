from django.shortcuts import render, HttpResponse, redirect
from .models import Users
from django.contrib import messages
from django.core.urlresolvers import reverse


def login_registration(request):
	return render(request, "login_registration/index.html")

def login(request):
	result = Users.objects.login(request.POST)

	if result["created"] == False:
		return redirect(reverse('login_registration:login_registration'))
	
	else:
		res = Users.objects.login(request.POST)
		request.session['user_id'] = res['existing_user'].id
		return redirect(reverse('home:home'))


def process(request):
	if request.method == "POST":

		res = Users.objects.register(request.POST)
		if res ["created"]:
			register = res["created"]
			messages.success(request, "Sucess!")
			request.session['user_id'] = res['new_user'].id

		else:
			for error in res["errors"]:
				messages.error(request, error)
				return redirect(reverse('login_registration:login_registration'))
	
	return redirect(reverse('home:home'))

def logout(request):
    request.session.clear()
    return redirect(reverse('login_registration:login_registration'))
