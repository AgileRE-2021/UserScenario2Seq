# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

class project(models.Model):
    id_project = models.IntegerField(default=0)
    id_user = models.IntegerField(default=0)
    project_name = models.CharField(max_length=20)
    project_desc = models.TextField()
    date_created = models.DateTimeField ()
    last_updated = models.DateTimeField()

class feature(models.Model):
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    id_feature = models.IntegerField(default=0)
    feature_name = models.CharField(max_length=20)
    user_story = models.CharField(max_length=100)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()

class scenario(models.Model):
    feature = models.ForeignKey(feature, on_delete=models.CASCADE)
    id_scenario = models.IntegerField(default=0)
    tipe = models.CharField(max_length=25)
    content = models.CharField(max_length=75)

# Create your models here.

