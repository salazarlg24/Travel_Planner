from django.shortcuts import render,redirect
from . models import Trips, CombineTrip, Users
from django.core.urlresolvers import reverse
from django.contrib import messages
from datetime import datetime, date


# Create your views here.
def index(request):
	user = request.session['log_user_id'],
	# trip = Trips.objects.filter(user=user)

	# print CombineTrip.objects.all()
	context = {
	'user': Users.objects.get(id=request.session['log_user_id']),
	'usertrip':Trips.objects.filter(all_trips__user=user),
	'alltrip':Trips.objects.all().exclude(all_trips__user=user)
	}
	#user is getting the logged in users id
	#usertrip is matching that users id in the Combine table
	#alltrip is getting all the trips from Combine but excluding the user that is logged in
	

	return render(request,'blackbeltapp/index.html',context)

def destination(request,id):
	trip = Trips.objects.get(id=id)
	user = Users.objects.filter(all_users__user=id)
	context = {
	'dest': CombineTrip.objects.get(id=id),
	'alltrip':CombineTrip.objects.filter(trip=trip).exclude(user = user)
	}
	return render(request,'blackbeltapp/destination.html',context)

def add(request):
	# if str(request.POST['from']) < datetime.datetime.now():
	# 	messages.error(request,"Must be a future date")
	# 	return redirect(reverse('blackbelt:add'))

	return render(request,'blackbeltapp/add.html')

def join(request,id):
	jointrip = Trips.objects.get(id=id)
	joinuser = Users.objects.get(id=request.session['log_user_id'])
	verify = CombineTrip.objects.filter(trip=jointrip,user=joinuser)
	if not verify:
		CombineTrip.objects.create(trip=jointrip,user=joinuser)
	else:
		messages.error(request,'You already booked that trip. Please select another.')
	return redirect(reverse('blackbelt:index'))
	#jointrip is getting the trips id
	#joinuser is getting the users id from session
	#CombineTrip is creating trip and user bases on variables

def create(request):
	flag = True
	start = datetime.strptime(str(request.POST['from'])[:10], '%Y-%m-%d')
	end = datetime.strptime(str(request.POST['to'])[:10], '%Y-%m-%d')
	user = Users.objects.get(id=request.session['log_user_id'])

	if not Trips.objects.validdate(start):
		flag = False
		messages.error(request, "sorry Departure date must be future date")
	if not Trips.objects.comparedate(start,end):
		flag = False
		messages.error(request, "sorry Return date must be after Departure")
	if flag:
		trip = Trips.objects.create(destination=request.POST['destin'], description=request.POST['plan'], date_from= start, date_to= end, user = user)
		CombineTrip.objects.create(trip=trip,user=user)

		return redirect(reverse('blackbelt:index'))
	return redirect(reverse('blackbelt:add'))

	#trip is creating a trip.
	#user is grabbing the user id that logged in.
	#Combine is creating a trip and user based on the variable created.

