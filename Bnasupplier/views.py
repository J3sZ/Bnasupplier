from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView

# Create your views here.

class BnasupplierInfo (TemplateView):
    template_name = "bnasupplier.html"

