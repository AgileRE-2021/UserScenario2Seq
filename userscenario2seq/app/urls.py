# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path, include
import debug_toolbar

from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # # Main index page
    path('main', views.mainIndex, name='index'),

    # # Fitur page
    path('fitur', views.mainFitur, name='fitur'),
    
    # # Create Project Page
    path('create-project', views.createProject, name='create-project'),
    
    # # Tutorial page
    path('tutorial', views.tutorial, name='tutorial'),
    
    # # List Project Page
    path('list-project', views.listProject, name='list-project'),
    
    # Coba pakai id
    path('detail-project/<int:project_id>', views.detailProject, name='detail-project'),

    # # Edit Feature Page
    path('edit-feature/<int:project_id>/<int:feature_id>', views.editFeature, name='edit-feature'),

    # # Add Feature Page
    path('add-feature/', views.addFeature, name='add-feature'),
    path('add-feature/hasil', views.hasil, name='hasil'),
    path('__debug__/', include(debug_toolbar.urls)),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]