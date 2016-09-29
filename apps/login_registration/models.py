from __future__ import unicode_literals
import bcrypt
from django.db import models
import re


class UserManager(models.Manager):
	def register(self, data):
		errors = []
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		first_regex = re.compile(r'^.[a-zA-Z]')

		if not data["name"]:
			errors.append("Name field blank")

		if not first_regex.match(data["name"]):
			errors.append("Name field can only be letters")

		if not data["alias"]:
			errors.append("Alias field blank")

		if not data ["email"]:
			errors.append("Email field blank")

		if not EMAIL_REGEX.match(data['email']):
			errors.append("Must be valid email")
		
		else:
			existing_email = self.filter(email=data["email"])

			if existing_email:
				errors.append("Email already exists.")

		if not data["password"]:
			errors.append("Password field blank")

		if len(data["password"]) < 8:
			errors.append("Password field cannot be less than 8 characters")

		if not data["password"] == data["verify_password"]:
			errors.append("Passwords do not match")

		pw_hash = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())

		response = {}

		if errors:
			response["created"] = False
			response["errors"] = errors

		else:
			Epassword = data['password']
			hashedpass = bcrypt.hashpw(Epassword.encode(), bcrypt.gensalt())
			new_user = Users.objects.create(name = data["name"], alias=data["alias"],email = data["email"], password = hashedpass)
			response["created"] = True
			response["new_user"] = new_user
	

		return response

	def login(self, data):
		errors = []
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		response = {}
		existing_username= Users.objects.filter(email=data['email'])
		user = self.filter(email=data["email"])

		if not data['email']:
			errors.append("Email field blank")

		if not data['password']:
			errors.append("Eassword field blank")

		if not existing_username:
			errors.append("Email not recognized")

		password = data['password'].encode()
		if bcrypt.hashpw(password, user[0].password.encode()) == user[0].password:
			response["created"] = True


		else:
			errors.append("Email or password not recognized")

		response = {}

		if errors:
			response["created"] = False
			response["errors"] = errors


		else:
			response["created"] = True
			response["existing_user"] = user[0]
				
		return response


class Users(models.Model):
	name = models.CharField(max_length=50)
	alias = models.CharField(max_length=50)
	email = models.CharField(max_length=150)
	password = models.CharField(max_length=255)
	birth_date = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()
