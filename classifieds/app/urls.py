# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('services', views.services, name='services'),
    path('workers', views.workers, name='workers'),
    path('register/', views.register_auth, name='register'),
    path('register_auth/', views.register_user, name='register_user'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
