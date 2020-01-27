from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts import forms

# Create your views here.
class SignUp(CreateView):
    template_name = "accounts/signup.html"
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("accounts:login")
