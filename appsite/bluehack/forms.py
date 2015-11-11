from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User   # fill in custom user info then save it
from bluehack.models import CrisisUser
from django.contrib.auth.forms import UserCreationForm

class CrisisUserForm(ModelForm):
	class Meta:
		model = CrisisUser
		exclude = ['user']

	# def save(self, commit = True):
	# 	user = super(MyRegistrationForm, self).save(commit = False)
	# 	user.email = self.cleaned_data['email']
	#
	# 	if commit:
	# 		user.save()
	#
	# 	return user

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
