from django.views.generic import View
from django.shortcuts import render_to_response, get_object_or_404 ,render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django import get_version


def index(request):
    return render(request, 'common/home.html')
@login_required    
def dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')


def project_info(request):
    return render(request, 'workflow/project_info.html')

def introduction(request):
    return render(request, 'workflow/introduction.html')

def background(request):
    return render(request, 'workflow/background.html')

def prod_info(request):
    return render(request, 'workflow/prod_info.html')

def features(request):
    return render(request, 'workflow/features.html')

def non_func_1(request):
    return render(request, 'workflow/non_func_1.html')

def non_func_2(request):
    return render(request, 'workflow/non_func_2.html')

def non_func_3(request):
    return render(request, 'workflow/non_func_3.html')

def environment(request):
    return render(request, 'workflow/environment.html')

def add_dev_consideration(request):
    return render(request, 'workflow/add_dev_consideration.html')

def post_dev(request):
    return render(request, 'workflow/post_dev.html')

def use_case(request):
    return render(request, 'workflow/use_case.html')

def use_case(request):
    return render(request, 'workflow/use_case.html')

def io_config  (request):
    return render(request, 'workflow/io_config.html')







 

