from django.conf.urls import patterns, include, url
from django.contrib import admin
from projectspecs import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
    # Workflow urls
    url(r'^project-info/$',views.project_info),
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
)