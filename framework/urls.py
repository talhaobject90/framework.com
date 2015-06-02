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
    
    #include all urls from project specs
    url(r'^projectspecs/', include('projectspecs.urls')),

    
    
    
    
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



