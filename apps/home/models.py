from __future__ import unicode_literals
import bcrypt
from django.db import models
import re
from ..login_registration.models import Users

class UserManager(models.Manager):
	def add_quote(self, data, user_id):
		errors = []
		first_regex = re.compile(r'^.[a-zA-Z]')
		response = {}

		if not data["author"]:
			errors.append("Author field blank")

		if len(data["author"]) < 4:
			errors.append("Author field cannot be less than 3 characters")

		if not first_regex.match(data["author"]):
			errors.append("Author field can only be letters")

		if not data["quote"]:
			errors.append("Quote field blank")

		if len(data["quote"]) < 11:
			errors.append("Author field cannot be less than 3 characters")

		if errors:
			response["created"] = False
			response["errors"] = errors

		else:
			name = Users.objects.get(id = user_id)
			new_quote = Quotes.objects.create(author = data["author"], quote=data["quote"], FK_Users = name)
			response["created"] = True
			response["new_quote"] = new_quote
	

		return response

	def add_favorite(self, data, user_id):
		name = Users.objects.get(id = user_id)
		new_favorite = Add_favorite.objects.create(favorites = Quotes.objects.all())
		response["created"] = True
		response["new_fave"] = new_fave


class Quotes(models.Model):
	author = models.CharField(max_length=50)
	quote = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	FK_Users = models.ForeignKey(Users, related_name="Quote_User")
	count = models.ManyToManyField(Users, related_name='quote_count')
	objects = UserManager()

class Add_favorite(models.Model):
    favorites = models.ManyToManyField(Quotes, related_name='favorited_by')
    objects = UserManager()