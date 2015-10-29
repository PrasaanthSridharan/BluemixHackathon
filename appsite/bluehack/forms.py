from django import forms

class RegisterForm(forms.Form):
	username = forms.CharField(label='Username', max_length=20)
	password = forms.CharField(label='Password', max_length=20)
	email = forms.EmailField(label='Email', max_length=100)
	cellphone = forms.CharField(label='Cellphone', max_length=10, required=False)
	address = forms.CharField(label='address', max_length=100)