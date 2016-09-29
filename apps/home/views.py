from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from ..login_registration.models import Users
from .models import Quotes, Add_favorite

def home(request):
	if "user_id" in request.session:
		user = Users.objects.get(id = request.session['user_id'])
		quote_post = Quotes.objects.all().order_by('-created_at')
		favorite = Add_favorite.objects.all()
		context = {	
			'name': user.name,
			'quote_post':quote_post,
			'favorite':favorite
		}
		return render(request, "home/home.html", context)

	else:
		return redirect(reverse('login_registration:login_registration'))


def add_quote(request):
	if request.method == "POST":
		res = Quotes.objects.add_quote(request.POST, request.session['user_id'])
	if res["created"]:
		success_post = res["created"]
		request.session['quote_id'] = res['new_quote'].id

	else:
		for error in res["errors"]:
			messages.error(request, error)
			return redirect(reverse('home:home'))
	
	return redirect(reverse('home:home'))

def users(request, id):	
	if "user_id" in request.session:
		up = Quotes.objects.filter(id=id)
		user = Users.objects.get(id = request.session['user_id'])
		quote_post = Quotes.objects.all().order_by('-created_at')
		user_post = Quotes.objects.filter(id=up)
		context = {	
			'name': user.name,
			'quote_post':quote_post,
			'user_post': user_post
		}
		return render(request, "home/users.html", context)

	else:
		return redirect(reverse('login_registration:login_registration'))

def add_favorites(request):
	res = Add_favorite.objects.add_favorite(request.POST, request.session['user_id'])
	if res["created"]:
		success_post = res["created"]
		request.session['fave_id'] = res['new_fave'].id

	else:
		for error in res["errors"]:
			messages.error(request, error)
			return redirect(reverse('home:home'))
	
	return redirect(reverse('home:home'))