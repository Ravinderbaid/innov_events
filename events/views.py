from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from events.models import Events,User
from forms import MyRegistrationForm
import datetime

# Create your views here.
def index(request):
	files = Events.objects.order_by('-event_date')
	return render(request, 'home.html', {'files' :files})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")

def login_view(request):
	state = "Please log in below..."
	username = password = ''
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				state = "You're successfully logged in!"
				return HttpResponseRedirect("/")
			else:
				state = "Your account is not active, please contact the site admin."
		else:
			state = "Your username and/or password were incorrect."
	
	return render(request, 'login.html',{'state':state, 'username': username})

def signup(request):
	args = {}
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")
		else:
			args['form'] = form
	else:
		args['form'] = MyRegistrationForm()	
		args['form'].fields['email'].widget.attrs = {'class':'form-control input-lg'}
		args['form'].fields['username'].widget.attrs = {'class':'form-control input-lg'}
		args['form'].fields['password1'].widget.attrs = {'class':'form-control input-lg'}
		args['form'].fields['password2'].widget.attrs = {'class':'form-control input-lg'}
		args['form'].fields['gender'].widget.attrs = {'class':'form-control input-lg'}
	args.update(csrf(request))
	return render(request, 'signup.html', args)

@login_required(login_url = '/login/')
def events(request,event_id):
	event_detail=[]
	try:
		event_detail = Events.objects.get(pk=event_id)
		status = "Attend"
		user_list=[]
		expired = False
		users_attend = event_detail.users_attend.split(',')
		for user_id in users_attend:
			user_list.append(User.objects.get(pk=str(user_id)))
			if user_id == str(request.user.id):
				status = "Unattend"
		if datetime.date.today() > event_detail.event_date:
			expired = True
		return render(request,'event.html',{'user_list':user_list,'event_detail':event_detail,'status':status,'expired':expired})
	except Exception,e:
		raise Http404

@login_required(login_url = '/login/')
def attend(request,event_id):
	event_detail=[]
	try:
		event_detail = Events.objects.get(pk=event_id)
		status = request.POST.get('status')
		if status == "Unattend":
			user_list = event_detail.users_attend.split(',')
			print user_list
			user_list.remove(request.POST.get('user'))
			if user_list:
				event_detail.users_attend = ','.join(user_list)
			else:
				event_detail.users_attend =''
			status = 0
		else:
			if event_detail.users_attend:
				event_detail.users_attend+=","+str(request.user.id)
			else:
				event_detail.users_attend = str(request.user.id)
			status = 1
		event_detail.save()
		return HttpResponse(status)
	except Exception,e:
		raise Http404