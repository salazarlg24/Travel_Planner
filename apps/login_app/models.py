from __future__ import unicode_literals

from django.db import models
import bcrypt
# import re
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UsersManager(models.Manager):
	def validate(self,data):
		flag = True
		errors = []
		if len(data['name']) <= 2:
			flag = False
			errors.append('Name must be 3 characters or more.')
		if len(data['username']) <= 2:
			flag = False
			errors.append('Username must be 3 characters or more.')
		# if not EMAIL_REGEX.match(data['mail']):
		# 	flag = False
		# 	errors.append('Email must be a vaild email')
		if len(data['password']) <= 7:
			flag = False
			errors.append('Password must be 8 characters or more.')

		if data['password'] != data['cpass']:
			flag = False
			errors.append('Password Confirm must match Password')
		if flag:
			passverify = data['password']
			hashed = bcrypt.hashpw(str(passverify), bcrypt.gensalt())
			user = Users.objects.create (name = data['name'], user_name= data['username'], password = hashed )
			print Users.objects.all()
			return (True,user)
		else:
			return (False,errors)
			print Users.objects.all()

			
class Users(models.Model):
	name = models.CharField(max_length=255)
	user_name = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UsersManager()



