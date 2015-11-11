from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from models import CrisisUser
from forms import CrisisUserForm, UserForm
from django.forms.models import model_to_dict

def index(request):
	# Process the form data
	if request.method == "POST":
		crisisUserForm = CrisisUserForm(request.POST)
		userForm = UserForm(request.POST)
		assert crisisUserForm.is_valid()
		assert userForm.is_valid()
		if crisisUserForm.is_valid() and userForm.is_valid():
			crisisUserForm_data = crisisUserForm.cleaned_data
			userForm_data = userForm.cleaned_data
			new_user = User.objects.create_user(**userForm_data)
			new_user.save()
			crisis_user = CrisisUser.objects.create(user=new_user, **crisisUserForm_data)
			crisis_user.save()
			return HttpResponseRedirect(reverse('bluehack:register', args=(userForm_data['username'],)))

		return render(request, 'bluehack/index.html', {'error': 'Failed to register'})
	# Create a blank form if any other method
	else:
		crisisUserForm = CrisisUserForm()
		userForm = UserForm()
	return render(request, 'bluehack/index.html', {
		'error': '',
		'crisisUserForm': crisisUserForm,
		'userForm': userForm
		})

def register(request, username):
	user = User.objects.get(username=username)
	password = user.password
	email = user.email
	cellphone = user.crisisuser.cellphone
	address = user.crisisuser.address
	context = {
				'userProps': model_to_dict(user, fields=['username', 'password', 'email']),
				'crisisUserProps': model_to_dict(user.crisisuser)
			  }
	return render(request, 'bluehack/register.html', context)
