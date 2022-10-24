from django.urls import re_path
from app_four import views


app_name = 'app_four'

urlpatterns = [
    re_path(r'^relative/$', views.relative, name='relative'),
    re_path(r'^other/$', views.other, name='other'),
    
    
]
