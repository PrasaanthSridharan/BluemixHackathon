from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from models import CrisisUser
from forms import RegisterForm

def index(request):
	# Process the form data
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form_data = form.cleaned_data
			new_user = User.objects.create_user(form_data['username'], form_data['email'], form_data['password'])
			new_user.save()
			crisis_user = CrisisUser(user=new_user, cellphone=form_data['cellphone'], address=form_data['address'])
			crisis_user.save()
			return HttpResponseRedirect(reverse('bluehack:register', args=(form_data['username'],)))
	
		return render(request, 'bluehack/index.html', {'error': 'Failed to register'})
	# Create a blank form if any other method
	else:
		form = RegisterForm()
	return render(request, 'bluehack/index.html', {'error': '', 'form': form})

def register(request, username):
	user = User.objects.get(username=username)
	password = user.password
	email = user.email
	cellphone = user.crisisuser.cellphone
	address = user.crisisuser.address
	context = {
				'username': username,
				'password': password,
				'email': email,
				'cellphone': cellphone,
				'address': address
			  }
	return render(request, 'bluehack/register.html', context)
