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
    
    # # Create Project Page
    path('create-project', views.createProject, name='create-project'),
    
    # # Tutorial page
    path('tutorial', views.tutorial, name='tutorial'),
    
    # # List Project Page
    path('list-project', views.listProject, name='list-project'),

<<<<<<< HEAD
    # # Edit Project Page
    path('edit-project/<int:user_id>/<int:project_id>', views.editFeature, name='edit-feature'),

    # Delete Project
    path('delete-project/<int:project_id>', views.deleteProject, name='delete-project'),

    # Delete Feature
    path('delete-feature/<int:feature_id>', views.deleteFeature, name='delete-feature'),

    # Coba pakai id
    path('detail-project/<int:project_id>', views.detailProject, name='detail-project'),

    # # Edit Feature Page
    path('edit-feature/<int:project_id>/<int:feature_id>', views.editFeature, name='edit-feature'),
<<<<<<< HEAD

    # # Add Feature Page
    path('add-feature/<int:project_id>', views.addFeature, name='add-feature'),
=======
    path('edit-feature/update', views.updateFeature, name='edit-feature'),

    # # Add Feature Page
    path('add-feature/<int:project_id>', views.addFeature, name='add-feature'),
    path('add-feature/store', views.addFeatureHasil, name='add-feature-hasil'),
>>>>>>> 4205d106b736c50a7307bf9cd1af0bcd917e86af

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
