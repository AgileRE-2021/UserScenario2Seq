# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.template import loader
from django.http import HttpResponse
from django import template
from app.models import project, feature, scenario
from django.utils import timezone


@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def mainIndex(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'main/index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def mainFitur(request):
    
    context = {}
    context['segment'] = 'fitur'

    return render(request, 'main/fitur.html', {'context': context})

@login_required(login_url="/login/")
def tutorial(request):
    
    context = {}
    context['segment'] = 'tutorial'

    return render(request, 'main/tutorial.html', {'context': context})

@login_required(login_url="/login/")
def createProject(request):
    
    project_name = request.POST.get("project_name")
    project_desc = request.POST.get("project_desc")
    content  = request.POST.get("content")

    return render(request, 'main/create-project.html')

@login_required(login_url="/login/")
def listProject(request):
    
    context = {}
    
    context['segment'] = 'listProject'
    
    context['project'] = project.objects.filter(id_user=request.user.id) #ambil record project dari model
    #request.user adalah user yang sedang login
    
    context['user'] = request.user
    #segment, user, dan project adalah key dari object context

    return render(request, 'main/list-project.html', {'context': context})

@login_required(login_url="/login/")
def deleteProject(request, project_id):
    project_to_delete = get_object_or_404(project, pk=project_id).delete()
    return redirect('list-project') #list-project adalah name dari url


@login_required(login_url="/login/")
def detailProject(request, project_id):
    
    context = {}
    #project_to_edit = get_object_or_404(project, pk=project_id)

    #project_to_edit.project_desc = "ini deskripsi baruu banget"
    #project_to_edit.last_updated = timezone.now()
    #project_to_edit.save()
    
    context['project'] = get_object_or_404(project, pk=project_id)

    #html_template = loader.get_template( 'main/detail-project.html' )
    return render(request, 'main/detail-project.html', {'context': context})
    #return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def addFeature(request, project_id):
    
    context = {}
    context['project_id'] = project_id
    context['project'] = get_object_or_404(project, pk=project_id)
  
    #html_template = loader.get_template( 'main/detail-project.html' )
    return render(request, 'main/add-feature.html', {'context': context})

@login_required(login_url="/login/")
def addFeatureHasil(request):
    
    getProject = get_object_or_404(project, pk=request.POST.get("project_id"))
    featureName = request.POST.get("featureName")
    userStory = request.POST.get("userStory")
    dateCreated = timezone.now()
    lastUpdated = timezone.now()
    tipe1 = request.POST.get("tipe1")
    content1  = request.POST.get("content1")
    tipe2 = request.POST.get("tipe2")
    content2  = request.POST.get("content2")
    tipe3 = request.POST.get("tipe3")
    content3  = request.POST.get("content3")
    
    #create feature baru
    newFeature = feature(project=getProject
                        ,feature_name=featureName
                        ,user_story=userStory
                        ,date_created=dateCreated
                        ,last_updated=lastUpdated)

    #save feature baru
    newFeature.save()

    #get feature terbaru
    getFeature = feature.objects.filter(project=getProject).order_by('-date_created')[0]

    #create scenario form
    newScenario1 = scenario(feature=getFeature
                        ,tipe=tipe1
                        ,content=content1
                        ,date_created=dateCreated
                        ,last_updated=lastUpdated)

    #save scenario baru
    newScenario1.save()

    newScenario2 = scenario(feature=getFeature
                        ,tipe=tipe2
                        ,content=content2
                        ,date_created=dateCreated
                        ,last_updated=lastUpdated)

    #save scenario baru
    newScenario2.save()

    newScenario3 = scenario(feature=getFeature
                        ,tipe=tipe3
                        ,content=content3
                        ,date_created=dateCreated
                        ,last_updated=lastUpdated)

    #save scenario baru
    newScenario3.save()
  
    #html_template = loader.get_template( 'main/detail-project.html' )
    return redirect('detail-project', project_id=request.POST.get("project_id"))

@login_required(login_url="/login/")
def editFeature(request, project_id, feature_id):
    
    context = {}
    context['project_id'] = project_id
    context['project'] = get_object_or_404(project, pk=project_id)

    #mengambil feature
    context['feature_id'] = feature_id
    context['feature'] = get_object_or_404(feature, pk=feature_id)

    #mengambil scenario
    context['scenarios'] = scenario.objects.filter(feature=context['feature'])

    #html_template = loader.get_template( 'main/detail-project.html' )
    return render(request, 'main/edit-feature.html', {'context': context})

@login_required(login_url="/login/")
def updateFeature(request):
    
    project_to_edit = get_object_or_404(project, pk=request.POST.get("project_id"))
    feature_to_edit = get_object_or_404(feature, pk=request.POST.get("feature_id"))
    featureName = request.POST.get("featureName")
    userStory = request.POST.get("userStory")
    dateCreated = timezone.now()
    lastUpdated = timezone.now()
    tipe1 = request.POST.get("tipe1")
    content1  = request.POST.get("content1")
    tipe2 = request.POST.get("tipe2")
    content2  = request.POST.get("content2")
    tipe3 = request.POST.get("tipe3")
    content3  = request.POST.get("content3")

    #update feature baru
    feature_to_edit.feature_name = featureName
    feature_to_edit.user_story = userStory
    feature_to_edit.last_updated = lastUpdated

    #save feature baru
    feature_to_edit.save()

    scenario_to_edit1 = scenario.objects.filter(feature=feature_to_edit).update(tipe=tipe1, content=content1)
    scenario_to_edit1.save()

    scenario_to_edit2 = scenario.objects.filter(feature=feature_to_edit).update(tipe=tipe2, content=content2)
    scenario_to_edit2.save()

    scenario_to_edit3 = scenario.objects.filter(feature=feature_to_edit).update(tipe=tipe3, content=content3)
    scenario_to_edit3.save()

    #html_template = loader.get_template( 'main/detail-project.html' )
    return redirect('detail-project',  project_id=request.POST.get("project_id"))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
