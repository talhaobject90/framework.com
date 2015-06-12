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
from forms import *


tinydb_pathto_file = "{0}/db/tinydb.json"
tinydb_path = tinydb_pathto_file.format(settings.PROJECT_ROOT)
db = TinyDB(tinydb_path)

def project_info(request):
    
    if request.method == 'POST':
            # check cookie set
            eid = request.session.get('eid',len(db)+1)
            
            el = db.get(None,eid)
            # if new data
            if(el == None):
                insert_data = request.POST
                db.insert(insert_data)
                request.session['eid'] = eid
                el = db.get(None, eid)
            # if update     
            else:
                eid = request.session.get('eid',len(db)+1)
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
                db.update(update_data,eids = [eid])
                el = db.get(None, eid)

            open_el = db.search(where('file_name'))
            open_el_array = {}            
            for open_el_mem in open_el:
                open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
            
            file_name = el['file_name']
         
            context_data = {'json_data': el,
                            'file_name':file_name,
                            'open_el_array':open_el_array}
            return render_to_response(
            'workflow/project_info.html',
            context_data,  
            RequestContext(request)
            )
    else:
        # opening existing session 
        
        if (request.session.get('eid',None)  != None):
                eid = request.session.get('eid',len(db)+1)
                el = db.get(cond=None, eid =  int(eid))
                
                json_data = el
                file_name = el['file_name']
                
        #opening new session
        else:
            json_data =""
            file_name = ''
            
        open_el = db.search(where('file_name'))
        open_el_array = {}
        
        for open_el_mem in open_el:
            open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
  
        context_data = {'json_data':    json_data,
                        'file_name':file_name,
                        'open_el_array':open_el_array} 
        return render_to_response(
        'workflow/project_info.html',
        context_data,  
        RequestContext(request)
        )


def new_project(request):
        if request.session.get('eid', None) != None:
            del request.session['eid']
        return HttpResponseRedirect("/projectspecs/project-info/")

def open_project(request ,eid = None):
        
        if request.session.get('eid', None) != None:
          del request.session['eid']
        
        
        if eid:
            request.session['eid'] = int(eid)
            #return HttpResponse(request.session['eid'])
            return HttpResponseRedirect("/projectspecs/project-info/")
        else:
            return HttpResponseRedirect("/projectspecs/project-info/")
            
    
     
def introduction(request):
    
    if request.method == 'POST':
        
            # check cookie set
            eid = request.session.get('eid',len(db)+1)
            
            el = db.get(None,eid)
            # if new data
            if(el == None):
                insert_data = request.POST
                db.insert(insert_data)
                request.session['eid'] = eid
                el = db.get(None, eid)
            # if update     
            else:
                eid = request.session.get('eid',len(db)+1)
                update_data = request.POST
                update_data = {"purpose": request.POST.get("purpose", "purpose"),
                               "scope": request.POST.get("scope", "scope"),
                               "reference": request.POST.get("reference", "reference"),
                               "standards": request.POST.get("standards", "standards")}
                db.update(update_data,eids = [eid])
                el = db.get(None, eid)
            open_el = db.search(where('file_name'))
            open_el_array = {}   
            for open_el_mem in open_el:
                open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
            
            file_name = el['file_name']
         
            context_data = {'json_data': el,
                            'file_name':file_name,
                            'open_el_array':open_el_array}
                        
            return render_to_response(
            'workflow/introduction.html',
            context_data,  
            RequestContext(request)
            )
    else:
        # opening existing session 
        if (request.session.get('eid',None)  != None):
                eid = request.session.get('eid',len(db)+1)
                el = db.get(cond=None, eid =  int(eid))
                
                json_data = el
                file_name = el['file_name']
                
        #opening new session
        else:
            json_data =""
            file_name = ''
            
        open_el = db.search(where('file_name'))
        open_el_array = {}
        
        for open_el_mem in open_el:
            open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
  
        context_data = {'json_data':    json_data,
                        'file_name':file_name,
                        'open_el_array':open_el_array} 
        return render_to_response(
        'workflow/introduction.html',
        context_data,  
        RequestContext(request)
        )
    
    
 

def background(request):

    if request.method == 'POST':
        
            # check cookie set
            eid = request.session.get('eid',len(db)+1)
            
            el = db.get(None,eid)
            # if new data
            if(el == None):
                insert_data = request.POST
                db.insert(insert_data)
                request.session['eid'] = eid
                el = db.get(None, eid)
            # if update     
            else:
                eid = request.session.get('eid',len(db)+1)
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
                db.update(update_data,eids = [eid])
                el = db.get(None, eid)
            open_el = db.search(where('file_name'))
            open_el_array = {}   
            for open_el_mem in open_el:
                open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
            
            file_name = el['file_name']
         
            context_data = {'json_data': el,
                            'file_name':file_name,
                            'open_el_array':open_el_array}
            return render_to_response(
            'workflow/background.html',
            context_data,  
            RequestContext(request)
            )
    else:
        # opening existing session 
        if (request.session.get('eid',None)  != None):
                eid = request.session.get('eid',len(db)+1)
                el = db.get(cond=None, eid =  int(eid))
                
                json_data = el
                file_name = el['file_name']
                
        #opening new session
        else:
            json_data =""
            file_name = ''
            
        open_el = db.search(where('file_name'))
        open_el_array = {}
 
        for open_el_mem in open_el:
            open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
  
        context_data = {'json_data':    json_data,
                        'file_name':file_name,
                        'open_el_array':open_el_array} 
        return render_to_response(
        'workflow/background.html',
        context_data,  
        RequestContext(request)
        )

def prod_info(request):

    
    if request.method == 'POST':
        
            # check cookie set
            eid = request.session.get('eid',len(db)+1)
            
            el = db.get(None,eid)
            # if new data
            if(el == None):
                insert_data = request.POST
                db.insert(insert_data)
                request.session['eid'] = eid
                el = db.get(None, eid)
            # if update     
            else:
                eid = request.session.get('eid',len(db)+1)
                update_data = request.POST
                update_data = {"prod_info": request.POST.get("prod_info", "prod_info"),
                               "prod_viewpoints": request.POST.get("prod_viewpoints", "prod_viewpoints"),
                               "major_prod_constraints": request.POST.get("major_prod_constraints", "major_prod_constraints")}
                db.update(update_data,eids = [eid])
                el = db.get(None, eid)
            open_el = db.search(where('file_name'))
            open_el_array = {}   
            for open_el_mem in open_el:
                open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
            
            file_name = el['file_name']
         
            context_data = {'json_data': el,
                            'file_name':file_name,
                            'open_el_array':open_el_array}
            return render_to_response(
            'workflow/prod_info.html',
            context_data,  
            RequestContext(request)
            )
    else:
        # opening existing session 
        if (request.session.get('eid',None)  != None):
                eid = request.session.get('eid',len(db)+1)
                el = db.get(cond=None, eid =  int(eid))
                
                json_data = el
                file_name = el['file_name']
                
        #opening new session
        else:
            json_data =""
            file_name = ''
            
        open_el = db.search(where('file_name'))
        open_el_array = {}
        
        for open_el_mem in open_el:
            open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
  
        context_data = {'json_data':    json_data,
                        'file_name':file_name,
                        'open_el_array':open_el_array} 
        return render_to_response(
        'workflow/prod_info.html',
        context_data,  
        RequestContext(request)
        )


def features(request):
    return render(request, 'workflow/features.html')

def non_func_1(request):


    if request.method == 'POST':
        
            # check cookie set
            eid = request.session.get('eid',len(db)+1)
            
            el = db.get(None,eid)
            # if new data
            if(el == None):
                insert_data = request.POST
                db.insert(insert_data)
                request.session['eid'] = eid
                el = db.get(None, eid)
            # if update     
            else:
                eid = request.session.get('eid',len(db)+1)
                update_data = request.POST
                update_data = {"system_req": request.POST.get("system_req", "system_req"),
                               "tech_req": request.POST.get("tech_req", "tech_req"),
                               "startup_req": request.POST.get("startup_req", "startup_req"),
                               "shutdown_req": request.POST.get("shutdown_req", "shutdown_req"),
                               "interface_req": request.POST.get("interface_req", "interface_req"),
                               "prob_req": request.POST.get("prob_req", "prob_req"),
                               "performance_req": request.POST.get("performance_req", "performance_req")}
                db.update(update_data,eids = [eid])
                el = db.get(None, eid)
            open_el = db.search(where('file_name'))
            open_el_array = {}   
            for open_el_mem in open_el:
                open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
            
            file_name = el['file_name']
         
            context_data = {'json_data': el,
                            'file_name':file_name,
                            'open_el_array':open_el_array}
            return render_to_response(
            'workflow/non_func_1.html',
            context_data,  
            RequestContext(request)
            )
    else:
        # opening existing session 
        if (request.session.get('eid',None)  != None):
                eid = request.session.get('eid',len(db)+1)
                el = db.get(cond=None, eid =  int(eid))
                
                json_data = el
                file_name = el['file_name']
                
        #opening new session
        else:
            json_data =""
            file_name = ''
            
        open_el = db.search(where('file_name'))
        open_el_array = {}
        
        for open_el_mem in open_el:
            open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
  
        context_data = {'json_data':    json_data,
                        'file_name':file_name,
                        'open_el_array':open_el_array} 
        return render_to_response(
        'workflow/non_func_1.html',
        context_data,  
        RequestContext(request)
        )

def non_func_2(request):
    
        if request.method == 'POST':
        
            # check cookie set
            eid = request.session.get('eid',len(db)+1)
            
            el = db.get(None,eid)
            # if new data
            if(el == None):
                insert_data = request.POST
                db.insert(insert_data)
                request.session['eid'] = eid
                el = db.get(None, eid)
            # if update     
            else:
                eid = request.session.get('eid',len(db)+1)
                update_data = request.POST
                update_data = {"reliability_req": request.POST.get("reliability_req", "reliability_req"),
                               "supp_req": request.POST.get("supp_req", "supp_req"),
                               "impl_req": request.POST.get("impl_req", "impl_req"),
                               "op_env_req": request.POST.get("op_env_req", "op_env_req"),
                               "usablity_req": request.POST.get("usablity_req", "usablity_req"),
                               "sec_req": request.POST.get("sec_req", "sec_req"),
                               "qual_req": request.POST.get("qual_req", "qual_req")}
                db.update(update_data,eids = [eid])
                el = db.get(None, eid)
            open_el = db.search(where('file_name'))
            open_el_array = {}   
            for open_el_mem in open_el:
                open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
            
            file_name = el['file_name']
         
            context_data = {'json_data': el,
                            'file_name':file_name,
                            'open_el_array':open_el_array}
            return render_to_response(
            'workflow/non_func_2.html',
            context_data,  
            RequestContext(request)
            )
        else:
            # opening existing session 
            if (request.session.get('eid',None)  != None):
                    eid = request.session.get('eid',len(db)+1)
                    el = db.get(cond=None, eid =  int(eid))
                    
                    json_data = el
                    file_name = el['file_name']
                    
            #opening new session
            else:
                json_data =""
                file_name = ''
                
            open_el = db.search(where('file_name'))
            open_el_array = {}
            
            for open_el_mem in open_el:
                open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
      
            context_data = {'json_data':    json_data,
                            'file_name':file_name,
                            'open_el_array':open_el_array} 
            return render_to_response(
            'workflow/non_func_2.html',
            context_data,  
            RequestContext(request)
            )


def non_func_3(request):

    
        if request.method == 'POST':
        
            # check cookie set
            eid = request.session.get('eid',len(db)+1)
            
            el = db.get(None,eid)
            # if new data
            if(el == None):
                insert_data = request.POST
                db.insert(insert_data)
                request.session['eid'] = eid
                el = db.get(None, eid)
            # if update     
            else:
                eid = request.session.get('eid',len(db)+1)
                update_data = request.POST
                update_data = {"trace_req": request.POST.get("trace_req", "trace_req"),
                               "config_req": request.POST.get("config_req", "config_req"),
                               "err_handling_req": request.POST.get("err_handling_req", "err_handling_req"),
                               "localization_req": request.POST.get("localization_req", "localization_req"),
                               "online_help_req": request.POST.get("online_help_req", "online_help_req"),
                               "reporting_req": request.POST.get("reporting_req", "reporting_req"),
                               "assumptions": request.POST.get("assumptions", "assumptions")}
                db.update(update_data,eids = [eid])
                el = db.get(None, eid)
            open_el = db.search(where('file_name'))
            open_el_array = {}   
            for open_el_mem in open_el:
                open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
            
            file_name = el['file_name']
         
            context_data = {'json_data': el,
                            'file_name':file_name,
                            'open_el_array':open_el_array}
            return render_to_response(
            'workflow/non_func_3.html',
            context_data,  
            RequestContext(request)
            )
        else:
            # opening existing session 
            if (request.session.get('eid',None)  != None):
                    eid = request.session.get('eid',len(db)+1)
                    el = db.get(cond=None, eid =  int(eid))
                    
                    json_data = el
                    file_name = el['file_name']
                    
            #opening new session
            else:
                json_data =""
                file_name = ''
                
            open_el = db.search(where('file_name'))
            open_el_array = {}
            
            for open_el_mem in open_el:
                open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
      
            context_data = {'json_data':    json_data,
                            'file_name':file_name,
                            'open_el_array':open_el_array} 
            return render_to_response(
            'workflow/non_func_3.html',
            context_data,  
            RequestContext(request)
            )


def environment(request):
        if request.method == 'POST':
        
            # check cookie set
            eid = request.session.get('eid',len(db)+1)
            
            el = db.get(None,eid)
            # if new data
            if(el == None):
                insert_data = request.POST
                db.insert(insert_data)
                request.session['eid'] = eid
                el = db.get(None, eid)
            # if update     
            else:
                eid = request.session.get('eid',len(db)+1)
                update_data = request.POST
                update_data = {"dev_hardware_req": request.POST.get("dev_hardware_req", "dev_hardware_req"),
                               "dev_software_req": request.POST.get("dev_software_req", "dev_software_req"),
                               "dev_deviations": request.POST.get("dev_deviations", "dev_deviations"),
                               "target_hardware_req": request.POST.get("target_hardware_req", "target_hardware_req"),
                               "target_software_req": request.POST.get("target_software_req", "target_software_req"),
                               "target_deviations": request.POST.get("target_deviations", "target_deviations")}
                db.update(update_data,eids = [eid])
                el = db.get(None, eid)
            open_el = db.search(where('file_name'))
            open_el_array = {}   
            for open_el_mem in open_el:
                open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
            
            file_name = el['file_name']
         
            context_data = {'json_data': el,
                            'file_name':file_name,
                            'open_el_array':open_el_array}
            return render_to_response(
            'workflow/environment.html',
            context_data,  
            RequestContext(request)
            )
        else:
            # opening existing session 
            if (request.session.get('eid',None)  != None):
                    eid = request.session.get('eid',len(db)+1)
                    el = db.get(cond=None, eid =  int(eid))
                    
                    json_data = el
                    file_name = el['file_name']
                    
            #opening new session
            else:
                json_data =""
                file_name = ''
                
            open_el = db.search(where('file_name'))
            open_el_array = {}
            
            for open_el_mem in open_el:
                open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
      
            context_data = {'json_data':    json_data,
                            'file_name':file_name,
                            'open_el_array':open_el_array} 
            return render_to_response(
            'workflow/environment.html',
            context_data,  
            RequestContext(request)
            )


def add_dev_consideration(request):

        if request.method == 'POST':
        
            # check cookie set
            eid = request.session.get('eid',len(db)+1)
            
            el = db.get(None,eid)
            # if new data
            if(el == None):
                insert_data = request.POST
                db.insert(insert_data)
                request.session['eid'] = eid
                el = db.get(None, eid)
            # if update     
            else:
                eid = request.session.get('eid',len(db)+1)
                update_data = request.POST
                update_data = {"cust_part_req": request.POST.get("cust_part_req", "cust_part_req"),
                               "commn_req": request.POST.get("commn_req", "commn_req"),
                               "infrastructure_req": request.POST.get("infrastructure_req", "infrastructure_req")}
                db.update(update_data,eids = [eid])
                el = db.get(None, eid)
            open_el = db.search(where('file_name'))
            open_el_array = {}   
            for open_el_mem in open_el:
                open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
            
            file_name = el['file_name']
         
            context_data = {'json_data': el,
                            'file_name':file_name,
                            'open_el_array':open_el_array}
            return render_to_response(
            'workflow/add_dev_consideration.html',
            context_data,  
            RequestContext(request)
            )
        else:
            # opening existing session 
            if (request.session.get('eid',None)  != None):
                    eid = request.session.get('eid',len(db)+1)
                    el = db.get(cond=None, eid =  int(eid))
                    
                    json_data = el
                    file_name = el['file_name']
                    
            #opening new session
            else:
                json_data =""
                file_name = ''
                
            open_el = db.search(where('file_name'))
            open_el_array = {}
            
            for open_el_mem in open_el:
                open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
      
            context_data = {'json_data':    json_data,
                            'file_name':file_name,
                            'open_el_array':open_el_array} 
            return render_to_response(
            'workflow/add_dev_consideration.html',
            context_data,  
            RequestContext(request)
            )


def post_dev(request):

        if request.method == 'POST':
        
            # check cookie set
            eid = request.session.get('eid',len(db)+1)
            
            el = db.get(None,eid)
            # if new data
            if(el == None):
                insert_data = request.POST
                db.insert(insert_data)
                request.session['eid'] = eid
                el = db.get(None, eid)
            # if update     
            else:
                eid = request.session.get('eid',len(db)+1)
                update_data = request.POST
                update_data = {"tech_transfer_req": request.POST.get("tech_transfer_req", "tech_transfer_req"),
                               "maintenance_req": request.POST.get("maintenance_req", "maintenance_req")}
                db.update(update_data,eids = [eid])
                el = db.get(None, eid)
            open_el = db.search(where('file_name'))
            open_el_array = {}   
            for open_el_mem in open_el:
                open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
            
            file_name = el['file_name']
         
            context_data = {'json_data': el,
                            'file_name':file_name,
                            'open_el_array':open_el_array}
            return render_to_response(
            'workflow/post_dev.html',
            context_data,  
            RequestContext(request)
            )
        else:
            # opening existing session 
            if (request.session.get('eid',None)  != None):
                    eid = request.session.get('eid',len(db)+1)
                    el = db.get(cond=None, eid =  int(eid))
                    
                    json_data = el
                    file_name = el['file_name']
                    
            #opening new session
            else:
                json_data =""
                file_name = ''
                
            open_el = db.search(where('file_name'))
            open_el_array = {}
            
            for open_el_mem in open_el:
                open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
      
            context_data = {'json_data':    json_data,
                            'file_name':file_name,
                            'open_el_array':open_el_array} 
            return render_to_response(
            'workflow/post_dev.html',
            context_data,  
            RequestContext(request)
            )


def use_case(request,puid = None):
    
        if request.method == 'POST':
            # check cookie set
            eid = request.session.get('eid',len(db)+1)
            
            el = db.get(None,eid)
            # if new data
            if(el == None):
                insert_data = request.POST
                db.insert(insert_data)
                request.session['eid'] = eid
                el = db.get(None, eid)
            # if update     
            else:
                eid = request.session.get('eid',len(db)+1)
                update_data = request.POST
                update_data = {"usecase":{"usercase_id": request.POST.get("usecase_id", "usecase_id"),
                               "usecase_name": request.POST.get("usecase_name", "usecase_name"),
                               "usercase_code_priority": request.POST.get("usecase_code_priority", "usecase_code_priority"),
                               "usecase_author": request.POST.get("usecase_author", "usecase_author"),
                               "usecase_date": request.POST.get("usecase_date", "usecase_date"),
                               "usecase_version": request.POST.get("usecase_version", "usecase_version"),
                               "usecase_actions": request.POST.get("usecase_actions", "usecase_actions"),
                               "usecase_frequency": request.POST.get("usecase_frequency", "usecase_frequency"),
                               "usecase_breif_desc": request.POST.get("usecase_breif_desc", "usecase_breif_desc"),
                               "usecase_pre_cond": request.POST.get("usecase_pre_cond", "usecase_pre_cond"),
                               "usecase_post_cond": request.POST.get("usecase_post_cond", "usecase_post_cond"),
                               "usecase_basic_flow": request.POST.get("usecase_basic_flow", "usecase_basic_flow"),
                               "usecase_alt_flow": request.POST.get("usecase_alt_flow", "usecase_alt_flow"),
                               "usecase_incl": request.POST.get("usecase_incl", "usecase_incl"),
                               "usecase_ext_point": request.POST.get("usecase_ext_point", "usecase_ext_point"),
                               "usecase_business_rules": request.POST.get("usecase_business_rules", "usecase_business_rules"),
                               "usecase_spl_req": request.POST.get("usecase_spl_req", "usecase_spl_req")}}
                db.update(update_data,eids = [eid])
                el = db.get(None, eid)
            open_el = db.search(where('file_name'))
            open_el_array = {}   
            for open_el_mem in open_el:
                open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
            
            file_name = el['file_name']
         
            context_data = {'json_data': el,
                            'file_name':file_name,
                            'open_el_array':open_el_array}
            return render_to_response(
            'workflow/use_case.html',
            context_data,  
            RequestContext(request)
            )  
        else:
            # opening existing session 
            
            #request.session['eid'] = 5
            
            #return HttpResponse(request.session.get('eid',None))
            
            if (request.session.get('eid',None)  != None):
                    eid = request.session.get('eid',len(db)+1)
                    el = db.get(cond=None, eid =  int(eid))
                    #return HttpResponse(el['usecase'])
                    
                    json_data = el
                    file_name = el['file_name']
                    all_data = db.all()
                    if (el['usecase']):
                        usecase_data = el['usecase']
                    else:
                        usecase_data = ""
                    
            #opening new session
            else:
                all_data = db.all()
                json_data =""
                file_name = ""
                usecase_data = ""
            
            #for usecase_data in jason_data:
            #return HttpResponse(json.dumps(json_data), content_type="application/json")
          
            #return HttpResponse(all_data)
            
            open_el = db.search(where('file_name'))
            open_el_array = {}
            
            for open_el_mem in open_el:
                open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
      
            context_data = {
                            'all_data': all_data,
                            'json_data':json_data,
                            'file_name':file_name,
                            'open_el_array':open_el_array,
                            'usecase_data': usecase_data # get usecase information
                            }
             
            return render_to_response(
            'workflow/use_case.html',
            context_data,  
            RequestContext(request)
            )


 

def io_config  (request):
    if request.method == 'POST':
        
            # check cookie set
            eid = request.session.get('eid',len(db)+1)
            
            el = db.get(None,eid)
            # if new data
            if(el == None):
                insert_data = request.POST
                db.insert(insert_data)
                request.session['eid'] = eid
                el = db.get(None, eid)
            # if update     
            else:
                eid = request.session.get('eid',len(db)+1)
                update_data = request.POST
                update_data = {"cust_code": request.POST.get("cust_code", "cust_code")}
                db.update(update_data,eids = [eid])
                el = db.get(None, eid)
            open_el = db.search(where('file_name'))
            open_el_array = {}   
            for open_el_mem in open_el:
                open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
            
            file_name = el['file_name']
         
            context_data = {'json_data': el,
                            'file_name':file_name,
                            'open_el_array':open_el_array}
            return render_to_response(
            'workflow/io_config.html',
            context_data,  
            RequestContext(request)
            )
    else:
        # opening existing session 
        if (request.session.get('eid',None)  != None):
                eid = request.session.get('eid',len(db)+1)
                el = db.get(cond=None, eid =  int(eid))
                
                json_data = el
                file_name = el['file_name']
                
        #opening new session
        else:
            json_data =""
            file_name = ''
            
        open_el = db.search(where('file_name'))
        open_el_array = {}
        
        for open_el_mem in open_el:
            open_el_array.update({open_el_mem.eid:open_el_mem['file_name']})
  
        context_data = {'json_data':    json_data,
                        'file_name':file_name,
                        'open_el_array':open_el_array} 
        return render_to_response(
        'workflow/io_config.html',
        context_data,  
        RequestContext(request)
        )
