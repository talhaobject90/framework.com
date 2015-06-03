from django.views.generic import View
from django.shortcuts import render_to_response, get_object_or_404 ,render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , HttpResponseRedirect
from django.core import serializers
from django.template import RequestContext
from django.conf import settings
import json
import os
from tinydb import TinyDB, where

tinydb_pathto_file = "{0}/db/tinydb.json"
tinydb_path = tinydb_pathto_file.format(settings.PROJECT_ROOT)
db = TinyDB(tinydb_path)
########## CUSTOM DATA ###
from forms import *



def project_info(request):
    
    
    if request.method == 'POST':
        
            # check cookie set
            project_code = request.POST.get("project_code", "newproject")
            
            el = db.get(where('project_code') == project_code)
            # if new data
            if(el == None):
                insert_data = request.POST
                db.insert(insert_data)
                request.session['project_code'] = project_code
                el = db.get(where('project_code') == project_code)
            # if update     
            else:
                project_code = request.session.get('project_code',None)
                update_data = request.POST
                update_data = {"cust_code": request.POST.get("cust_code", "cust_code"), 
                               "cust_addr": request.POST.get("cust_addr", "cust_addr"), 
                               "project_info": request.POST.get("project_info", "project_info"),
                               "database": request.POST.get("database", "database"),
                               "file_name": request.POST.get("file_name", "file_name"),
                               "cust_name": request.POST.get("cust_name", "cust_name"),
                               "project_code": request.POST.get("project_code", "project_code"),
                               "architecture": request.POST.get("architecture", "architecture"),
                               "prog_lang": request.POST.get("prog_lang", "prog_lang"),
                               "process_model": request.POST.get("process_model", "process_model")}
                db.update(update_data, where('project_code') == project_code)
                el = db.get(where('project_code') == project_code)
            
            context_data = {'json_data': el,
                            'project_code':request.session.get('project_code', None)}
            return render_to_response(
            'workflow/project_info.html',
            context_data,  
            RequestContext(request)
            )
    else:
        # opening existing session 
        if (request.session.get('project_code',None)  != 'New Project'):
                project_code = request.session.get('project_code',None)
                el = db.get(where('project_code') == project_code)
                json_data = el
        #opening new session
        else:
            json_data =""
            
        context_data = {'json_data':    json_data,
                        'project_code':request.session.get('project_code', "New Project")} 
        return render_to_response(
        'workflow/project_info.html',
        context_data,  
        RequestContext(request)
        )


def new_project(request):
        if request.session.get('project_code', None) != None:
            del request.session['project_code']
        return HttpResponseRedirect("/projectspecs/project-info/")
    
def introduction(request):
    
    if request.method == 'POST':
        
            # check cookie set
            project_code = request.session.get('project_code',None)
            
            el = db.get(where('project_code') == project_code)
            # if new data
            if(el == None):
                insert_data = request.POST
                db.insert(insert_data)
                request.session['project_code'] = project_code
                el = db.get(where('project_code') == project_code)
            # if update     
            else:
                project_code = request.session.get('project_code',None)
                update_data = request.POST
                update_data = {"purpose": request.POST.get("purpose", "purpose"),
                               "scope": request.POST.get("scope", "scope"),
                               "reference": request.POST.get("reference", "reference"),
                               "standards": request.POST.get("standards", "standards")}
                db.update(update_data, where('project_code') == project_code)
                el = db.get(where('project_code') == project_code)
            
            context_data = {'json_data': el,
                            'project_code':request.session.get('project_code', None)}
            return render_to_response(
            'workflow/introduction.html',
            context_data,  
            RequestContext(request)
            )
    else:
        # opening existing session 
        if (request.session.get('project_code',None)  != 'New Project'):
                project_code = request.session.get('project_code',None)
                el = db.get(where('project_code') == project_code)
                json_data = el
        #opening new session
        else:
            json_data =""
            
        context_data = {'json_data':    json_data,
                        'project_code':request.session.get('project_code', "New Project")} 
        return render_to_response(
        'workflow/introduction.html',
        context_data,  
        RequestContext(request)
        )
    
    
 

def background(request):

    if request.method == 'POST':
        
            # check cookie set
            project_code = request.session.get('project_code',None)
            
            el = db.get(where('project_code') == project_code)
            # if new data
            if(el == None):
                insert_data = request.POST
                db.insert(insert_data)
                request.session['project_code'] = project_code
                el = db.get(where('project_code') == project_code)
            # if update     
            else:
                project_code = request.session.get('project_code',None)
                update_data = request.POST
                update_data = {"the_problem_of": request.POST.get("the_problem_of", "the_problem_of"),
                               "affects": request.POST.get("affects", "affects"),
                               "the_impact_of_which": request.POST.get("the_impact_of_which", "the_impact_of_which"),
                               "success_soln": request.POST.get("success_soln", "success_soln"),
                               "input_for": request.POST.get("input_for", "input_for"),
                               "input_who": request.POST.get("input_who", "input_who"),
                               "prod_sys_name": request.POST.get("prod_sys_name", "prod_sys_name"),
                               "input_that": request.POST.get("input_that", "input_that"),
                               "input_unlike": request.POST.get("input_unlike", "input_unlike"),
                               "our_product": request.POST.get("our_product", "our_product")}
                db.update(update_data, where('project_code') == project_code)
                el = db.get(where('project_code') == project_code)
            
            context_data = {'json_data': el,
                            'project_code':request.session.get('project_code', None)}
            return render_to_response(
            'workflow/background.html',
            context_data,  
            RequestContext(request)
            )
    else:
        # opening existing session 
        if (request.session.get('project_code',None)  != 'New Project'):
                project_code = request.session.get('project_code',None)
                el = db.get(where('project_code') == project_code)
                json_data = el
        #opening new session
        else:
            json_data =""
            
        context_data = {'json_data':    json_data,
                        'project_code':request.session.get('project_code', "New Project")} 
        return render_to_response(
        'workflow/background.html',
        context_data,  
        RequestContext(request)
        )

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
    if request.method == 'POST':
        
            # check cookie set
            project_code = request.POST.get("project_code", "newproject")
            
            el = db.get(where('project_code') == project_code)
            # if new data
            if(el == None):
                insert_data = request.POST
                db.insert(insert_data)
                request.session['project_code'] = project_code
                el = db.get(where('project_code') == project_code)
            # if update     
            else:
                project_code = request.session.get('project_code',None)
                update_data = request.POST
                update_data = {"cust_code": request.POST.get("cust_code", "cust_code")}
                db.update(update_data, where('project_code') == project_code)
                el = db.get(where('project_code') == project_code)
            
            context_data = {'json_data': el,
                            'project_code':request.session.get('project_code', None)}
            return render_to_response(
            'workflow/io_config.html',
            context_data,  
            RequestContext(request)
            )
    else:
        # opening existing session 
        if (request.session.get('project_code',None)  != 'New Project'):
                project_code = request.session.get('project_code',None)
                el = db.get(where('project_code') == project_code)
                json_data = el
        #opening new session
        else:
            json_data =""
            
        context_data = {'json_data':    json_data,
                        'project_code':request.session.get('project_code', "New Project")} 
        return render_to_response(
        'workflow/io_config.html',
        context_data,  
        RequestContext(request)
        )
