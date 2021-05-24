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

    # # Fitur page
    path('help-and-documentation', views.helpAndDocumentation, name='help-and-documentation'),
    
    # # Create Project Page
    path('create-project', views.createProject, name='create-project'),

    # # Create Project Page
    path('create-project/store', views.createProjectStore, name='create-project-store'),
    
    # # Tutorial page
    path('tutorial', views.tutorial, name='tutorial'),
    
    # # List Project Page
    path('list-project', views.listProject, name='list-project'),

    # Delete Project
    path('delete-project/<int:project_id>', views.deleteProject, name='delete-project'),
    
    # Coba pakai id
    path('detail-project/<int:project_id>', views.detailProject, name='detail-project'),

    # # Edit Feature Page
    path('edit-feature/<int:project_id>/<int:feature_id>', views.editFeature, name='edit-feature'),

    # # Add Feature Page
    path('add-feature/<int:project_id>', views.addFeature, name='add-feature'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
