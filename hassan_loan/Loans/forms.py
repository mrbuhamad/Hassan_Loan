from django import forms
from .models import *
from django.contrib.auth.models import User   

class ParticipantsForm(forms.ModelForm):
	class Meta:
		model = Participants
		fields = ['name']

class holdamountForm(forms.ModelForm):
	class Meta:
		model = Hold_amount
		fields = ['part_hold_amount','date']


class Loanform(forms.ModelForm):
	class Meta:
		model = Loan
		fields = ['loan_amount','hold_amount','profit_amount',"date"]


class Pymentsform(forms.ModelForm):
	class Meta:
		model = Pyments
		fields = ['pyment','date']


class SignupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email' ,'password']

		widgets={
		'password': forms.PasswordInput(),
		}

class SigninForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())