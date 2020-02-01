from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib import messages
from . import models

class SuccessView(TemplateView):
   template_name = 'payment/success.html'

class CancelView(TemplateView):
   template_name = 'payment/cancel.html'

class ErrorView(TemplateView):
   template_name = 'payment/error.html'
   