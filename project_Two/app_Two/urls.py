from django.urls import re_path
from app_Two import views

urlpatterns = [
    re_path(r'^$', views.users, name='users'),
]
