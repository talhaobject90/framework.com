from django.views.generic import View
from django.shortcuts import render_to_response, get_object_or_404 ,render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django import get_version
from django.core import serializers
from django.template import RequestContext
from django.conf import settings
import json
########## CUSTOM DATA ###
from forms import MyForm


   

 

def index(request):
    return render(request, 'common/home.html')

@login_required    
def dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')


 

 





 

