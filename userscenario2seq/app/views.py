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
from app.models import project, feature, scenario, condition
from django.utils import timezone

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    #return HttpResponse(html_template.render(context, request))
    return redirect('tutorial')

@login_required(login_url="/login/")
def mainIndex(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'main/index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def helpAndDocumentation(request):
    
    context = {}
    context['segment'] = 'fitur'

    return render(request, 'main/help-and-documentation.html', {'context': context})

@login_required(login_url="/login/")
def tutorial(request):
    
    context = {}
    context['segment'] = 'tutorial'

    return render(request, 'main/tutorial.html', {'context': context})

@login_required(login_url="/login/")
def listProject(request):
    
    context = {}
    context['search'] = ""
    if(request.method == 'GET' and 'search' in request.GET):
        search = request.GET['search']
        if(search == ''):
            context['project'] = project.objects.filter(id_user=request.user.id) #ambil record project dari model
        else:
            context['project'] = project.objects.filter(id_user=request.user.id).filter(project_name__contains=search) #ambil record project dari model
            context['search'] = search
        #request.user adalah user yang sedang login
    else: 
        context['project'] = project.objects.filter(id_user=request.user.id) #ambil record project dari model
    
    context['user'] = request.user
    #segment, user, dan project adalah key dari object context

    return render(request, 'main/list-project.html', {'context': context})

@login_required(login_url="/login/")
def createProject(request):
    
    return render(request, 'main/create-project.html')

@login_required(login_url="/login/")
def createProjectStore(request):

    projectName= request.POST.get("project_name")
    projectDesc= request.POST.get("project_desc")
    date_created=timezone.now()
    last_updated=timezone.now()

    createProject = project(id_user=request.user.id
                    ,project_name=projectName
                    ,project_desc=projectDesc
                    ,date_created=date_created
                    ,last_updated=last_updated)

    createProject.save()
    return redirect ('list-project')

@login_required(login_url="/login/")
def deleteProject(request, project_id):
    project_to_delete = get_object_or_404(project, pk=project_id).delete()
    return redirect('list-project') #list-project adalah name dari url

@login_required(login_url="/login/")
def deleteFeature(request, feature_id,project_id):
    feature_to_delete = get_object_or_404(feature, pk=feature_id).delete()
    return redirect('detail-project', project_id=project_id)

@login_required(login_url="/login/")
def detailProject(request,project_id):
    context = {}
    context['id_project'] = project_id
    context['project'] = get_object_or_404(project, pk=project_id)
    context['search'] = ""

    if(request.method == 'GET' and 'search' in request.GET):
        search = request.GET['search']
        if(search == ''):
            context['feature'] = feature.objects.filter(project=context['project'])
        else:
            context['feature'] = feature.objects.filter(project=context['project']).filter(feature_name__contains=search)
            context['search'] = search
        #request.user adalah user yang sedang login
    else:
        context['feature'] = feature.objects.filter(project=context['project'])

    return render(request, 'main/detail-project.html', {'context': context})
    
@login_required(login_url="/login/")
def editProject(request, project_id):
    context = {}
    context['id_project'] = project_id
    context['project'] = get_object_or_404(project, pk=project_id)
    return render(request, 'main/edit-project.html', {'context': context}) 

@login_required(login_url="/login/")
def updateProject(request):
    context = {}
    project_to_edit = get_object_or_404(project, pk=request.POST.get("project_id"))
    projectName = request.POST.get("project_name")
    projectDesc = request.POST.get("project_desc")
    lastUpdated = timezone.now()
    project_to_edit.project_name = projectName
    project_to_edit.project_desc = projectDesc
    project_to_edit.last_updated = timezone.now()
    project_to_edit.save()
    return redirect('detail-project', project_id=request.POST.get("project_id")) 

@login_required(login_url="/login/")
def addFeature(request, project_id):
    
    context = {}
    context['project_id'] = project_id
    context['project'] = get_object_or_404(project, pk=project_id)
    counts = {}
  
    #html_template = loader.get_template( 'main/detail-project.html' )
    return render(request, 'main/add-feature.html', {'context': context})

@login_required(login_url="/login/")
def addFeatureHasil(request):
    getProject = get_object_or_404(project, pk=request.POST.get("project_id"))
    featureName = request.POST.get("featureName")
    userStory = request.POST.get("userStory")
    dateCreated = timezone.now()
    lastUpdated = timezone.now()

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

    #get jumlah scenario
    scenarioCount = request.POST.get("scenario-count")

    #get jumlah kondisi pada scenario normal
    baseConditionCount = request.POST.get("count0")
    for i in range(int(scenarioCount)):
        #looping sebanyak jumlah scenario
        keyScenarioName = request.POST.get("name"+str(i))

        if(i == 0):
            scenarioType = "Normal"
        else:
            scenarioType = "Alternative"
        
        #buat scenario
        newScenario = scenario(
            feature=getFeature,
            scenario_name=keyScenarioName,
            scenario_type=scenarioType,
            date_created=dateCreated,
            last_updated=lastUpdated
        )

        #save
        newScenario.save()

        #get scenario yang baru saja dibuat
        getScenario = scenario.objects.filter(feature=getFeature).filter(scenario_name=keyScenarioName).order_by('-date_created')[0]

        #jika scenario bukan scenario normal, maka tambahi dengan kondisi give when dari skenario normal
        if(i != 0):
            for k in range(int(baseConditionCount)):
                #looping sebanyak jumlah condition pada skenario normal
                
                #ambil jenis condition dari skenario normal untuk pengecekan
                conditionType = request.POST.get("scenario0-tipe"+str(k))

                if(conditionType != 'Then'):
                    #jika bukan Then, maka masukkan (berarti Given / When)

                    #buat condition
                    newCondition = condition(
                        scenario=getScenario,
                        tipe=request.POST.get("scenario0-tipe"+str(k)),
                        content=request.POST.get("scenario0-content"+str(k)),
                        date_created=dateCreated,
                        last_updated=lastUpdated
                    )

                    #save newCondition
                    newCondition.save()

        #get jumlah condition dalam scenario ke i
        conditionCount = request.POST.get("count"+str(i))

        for j in range(int(conditionCount)):
            #looping sebanyak jumlah condition

            #buat condition
            newCondition = condition(
                scenario=getScenario,
                tipe=request.POST.get("scenario"+str(i)+"-tipe"+str(j)),
                content=request.POST.get("scenario"+str(i)+"-content"+str(j)),
                date_created=dateCreated,
                last_updated=lastUpdated
            )

            #save newCondition
            newCondition.save()

    '''
    #create setiap scenario yang dibuat
    tipe = False
    content = False
    for key in request.POST:
        #hanya ambil request yg berhubungan sama scenario
        if(
            key != 'project_id' 
            and key != 'featureName' 
            and key != 'userStory'):

            if(tipe == False):
                #cek key adalah tipe atau content
                if("tipe" in key):
                    #masuk tipe
                    tipe = request.POST[key]
            
            if(content == False):
                if("content" in key):
                    #masuk content
                    content = request.POST[key]

            if(tipe != False and content != False):
                #create scenario form
                newScenario = scenario(feature=getFeature
                                    ,tipe=tipe
                                    ,content=content
                                    ,date_created=dateCreated
                                    ,last_updated=lastUpdated)

                #save scenario baru
                newScenario.save()
                tipe = False
                content = False
    '''
  
    #html_template = loader.get_template( 'main/detail-project.html' )
    return redirect('detail-project', project_id=request.POST.get("project_id"))

@login_required(login_url="/login/")
def editFeature(request, project_id, feature_id):
    
    context = {}
    context['project_id'] = project_id
    context['project'] = get_object_or_404(project, pk=project_id)

    #mengambil feature berdasarkan project
    context['feature_id'] = feature_id
    context['feature'] = get_object_or_404(feature, pk=feature_id)

    #mengambil scenario berdasarkan feature
    context['scenario'] = scenario.objects.filter(feature=context['feature'])

    #mengambil condition berdasarkan scenario
    context['condition'] = []
    for s in context['scenario']:
        context['condition'].append(condition.objects.filter(scenario=s))

    #html_template = loader.get_template( 'main/detail-project.html' )
    return render(request, 'main/edit-feature.html', {'context': context})

@login_required(login_url="/login/")
def updateFeature(request):
    
    #project_to_edit = get_object_or_404(project, pk=request.POST.get("project_id"))
    feature_to_edit = get_object_or_404(feature, pk=request.POST.get("feature_id"))
    featureName = request.POST.get("featureName")
    userStory = request.POST.get("userStory")
    dateCreated = timezone.now()
    lastUpdated = timezone.now()

    #update feature baru
    feature_to_edit.feature_name = featureName
    feature_to_edit.user_story = userStory
    feature_to_edit.last_updated = lastUpdated

    #save feature baru
    feature_to_edit.save()

    #ambil scenarios berdasarkan feature
    scenarioCount = int(request.POST.get('scenario-count'))
    for i in range(1,scenarioCount+1):
        scenarioId = request.POST.get('scenario'+str(i)+"-id")

        #get scenario berdasarkan id
        scenarioToUpdate = get_object_or_404(scenario, pk=scenarioId)
        print("id =",scenarioToUpdate.scenario_name)

        #update scenario
        scenarioToUpdate.scenario_name = request.POST.get('name'+str(i))
        scenarioToUpdate.last_updated = lastUpdated

        #save scenario
        scenarioToUpdate.save()

        for key in request.POST:
            #looping key dalam POST
            identifyScenario = "scenario"+str(scenarioId)
            identifyCondition = "condition"
            identifyId = "id"
            conditionId = ""

            if(
                identifyScenario in key 
                and identifyId in key
                and identifyCondition in key):
                #artinya ini name untuk id condition sesuai scenarioId
                conditionId = request.POST.get(key) #ambil id nya

                #ambil condition sesuai id
                conditionToUpdate = get_object_or_404(condition, pk=conditionId)

                #update
                conditionToUpdate.tipe = request.POST.get('scenario'+str(scenarioId)+'-condition'+str(conditionId)+'-tipe')
                conditionToUpdate.content = request.POST.get('scenario'+str(scenarioId)+'-condition'+str(conditionId)+'-content')
                conditionToUpdate.last_updated = lastUpdated

                #save
                conditionToUpdate.save()

    '''scenarios = scenario.objects.filter(feature=feature_to_edit)
    for s in scenarios:
        tipe = False
        content = False
        scenario_id = False
        for key in request.POST:
            #hanya ambil request yg berhubungan sama scenario
            if(
                key != 'project_id' 
                and key != 'feature_id'
                and key != 'featureName' 
                and key != 'userStory'):

                if(scenario_id == False):
                    if("scenario_id" in key):
                        #masuk scenario id
                        scenario_id = request.POST[key]

                if(tipe == False):
                    if("tipe" in key):
                        #masuk tipe
                        tipe = request.POST[key]
                
                if(content == False):
                    if("content" in key):
                        #masuk content
                        content = request.POST[key]
                
                if(tipe != False and content != False and scenario_id != False):

                    if(int(s.id_scenario) == int(scenario_id)):
                        #edit
                        s.tipe = tipe
                        s.content = content 
                        s.last_updated = lastUpdated

                        #save edit
                        s.save()

                    #kembalikan tipe, content, dan scenario id jadi false
                    tipe = False
                    content = False
                    scenario_id = False
    '''

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
