from django.views.generic import View
from django.shortcuts import render_to_response, get_object_or_404 ,render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , HttpResponseRedirect
from django.core import serializers
from django.template import RequestContext
from django.conf import settings
import json
import os
########## CUSTOM DATA ###
from forms import *



def project_info(request):
    if request.method == 'POST':
        # if the data is saved after opening
            data = json.dumps(request.POST)
            new_project_file = request.POST.get("file_name", "newproject")
            path_to_file = "{0}/db/"+new_project_file+".json"
            path = path_to_file.format(settings.PROJECT_ROOT)
            with open(path, "w") as out:
                out.write(data)
            request.session['file_name'] = new_project_file
            file_data = open(path)
            json_data = json.load(file_data)
            context_data = {'json_data': json_data}
            return render_to_response(
            'workflow/project_info.html',
            context_data,  
            RequestContext(request)
            )
    else:
        # opening existing session 
        if request.session.get('file_name', None): # if file name not saved
            path_to_file = "{0}/db/"+request.session['file_name']+".json"
            path = path_to_file.format(settings.PROJECT_ROOT)
            file_data = open(path)
            with open(path) as f:
                json_data = json.load(f)
        else:  # if new project is opened
            #del request.session['file_name']
            path = "{0}/db/tmp.json".format(settings.PROJECT_ROOT)
            json_data = ''
        context_data = {'json_data':    json_data,
                        'file_name':request.session.get('file_name', None)} 
        return render_to_response(
        'workflow/project_info.html',
        context_data,  
        RequestContext(request)
        )


def new_project(request):
        if request.session.get('file_name', None) != None:
            del request.session['file_name']
        return HttpResponseRedirect("/projectspecs/project-info/")
    
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

 


