from django.conf.urls import patterns, include, url
from django.contrib import admin
from framework import views
from login.views import *
from django.conf.urls.static import static
from django.conf import settings



admin.autodiscover()

urlpatterns = patterns('',
 
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/',views.dashboard, name='dashboard'),
    url(r'^dashboard/', 'django.contrib.auth.views.login'),
    
    # Register & Login URLs
    url(r'^logout/$', logout_page),
    url(r'^login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    
    # Workflow urls
    url(r'^project-info/',views.project_info),
    url(r'^introduction/',views.introduction),
    url(r'^background/',views.background),
    url(r'^prod-info/',views.prod_info),
    url(r'^features/',views.features),
    url(r'^non-func-1/',views.non_func_1),
    url(r'^non-func-2/',views.non_func_2),
    url(r'^non-func-3/',views.non_func_3),
    url(r'^environment/',views.environment),
    url(r'^add-dev-cons/',views.add_dev_consideration),
    url(r'^post-dev/',views.post_dev),
    url(r'^use-case/',views.use_case),
    url(r'^io-config/',views.io_config),
    
    
    
    
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



