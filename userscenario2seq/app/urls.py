# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # # Main index page
    path('main', views.mainIndex, name='index'),

    # Coba pakai id
    path('detail-project/<int:project_id>', views.detailProject, name='detail-project'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
