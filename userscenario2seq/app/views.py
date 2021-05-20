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
    
    context = {}
    context['segment'] = 'createProject'

    return render(request, 'main/create-project.html', {'context': context})

@login_required(login_url="/login/")
def listProject(request):
    
    context = {}
    context['segment'] = 'listProject'

    context['project'] = project.objects.filter(id_user=request.user.id)
    context['user'] = request.user

    return render(request, 'main/list-project.html', {'context': context})

@login_required(login_url="/login/")
def deleteProject(request, project_id):
    project_to_delete = get_object_or_404(project, pk=project_id).delete()
    return redirect('list-project')


@login_required(login_url="/login/")
def detailProject(request, project_id):
    
    context = {}
    context['id'] = project_id
    context['name'] = "Ini nama project"
    context['array'] = [project_id, "Ini nama project"]

    '''
    context = {
        segment: 'index',
    }
    '''


    #html_template = loader.get_template( 'main/detail-project.html' )
    return render(request, 'main/detail-project.html', {'context': context})
    #return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def addFeature(request, project_id):
    
    context = {}
    context['id'] = project_id
  
    #html_template = loader.get_template( 'main/detail-project.html' )
    return render(request, 'main/add-feature.html', {'context': context})

@login_required(login_url="/login/")
def editFeature(request, project_id, feature_id):
    
    context = {}
    context['idProject'] = project_id
    context['idFeature'] = feature_id
  
    #html_template = loader.get_template( 'main/detail-project.html' )
    return render(request, 'main/edit-feature.html', {'context': context})

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
