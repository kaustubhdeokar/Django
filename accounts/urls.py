from django.conf.urls import url
from . import views
from django.contrib.auth import login


urlpatterns = [
    url(r'^$',views.home),
    url(r'^login/$',views.login),
    
]