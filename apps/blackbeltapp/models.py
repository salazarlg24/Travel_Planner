from __future__ import unicode_literals

from django.db import models
from ..login_app.models import Users
from datetime import date, datetime

# Create your models here.
class TripsManager(models.Manager):
	def validdate(self,date):
		flag = True
		today = datetime.strptime(str(date.today())[:10],'%Y-%m-%d')
		diff = (date - today).days
		if diff <= 0:
			return False
		else:
			return True

	def comparedate(self, start, end):
		diff = (end - start).days
		if diff <= 0:
			return False
		else:
			return True


class Trips(models.Model):
	destination = models.CharField(max_length=255)
	description = models.TextField()
	date_from = models.DateTimeField(null=True, blank=True)
	date_to = models.DateTimeField(null=True, blank=True)
	user = models.ForeignKey(Users, related_name='user_on_trip')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = TripsManager()

class CombineTrip(models.Model):
	trip = models.ForeignKey(Trips, related_name='all_trips')
	user = models.ForeignKey(Users, related_name='all_users')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
