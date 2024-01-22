from django import forms
from acApp.models import user_table, User_profileinfo
from django.contrib.auth.models import User


class myNewForm(forms.ModelForm):
    class Meta:
        model = user_table
        fields = '__all__'


class mynewFormTwo(forms.Form):
    protfolio = forms.URLField()
    email = forms.EmailField()



##########today##############
class userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password",)


class userforminfo(forms.ModelForm):
    class Meta:
        model = User_profileinfo
        fields = ("portfolio_url", "profile_img")
