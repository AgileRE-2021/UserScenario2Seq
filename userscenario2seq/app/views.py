# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.template import loader
from django.conf import settings
from django.http import HttpResponse, Http404
from django import template
from app.models import project, feature, scenario, condition
from django.utils import timezone
from plantuml import PlantUML
from pathlib import Path
import os
from os.path import abspath

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
def generateSequence(request, feature_id,project_id):
    #ambil project
    project_to_generate = get_object_or_404(project, pk=project_id)

    #ambil fitur yang ingin digenerate
    feature_to_generate = get_object_or_404(feature, pk=feature_id)

    #ambil semua scenario sesuai fiturnya
    scenarios = scenario.objects.filter(feature=feature_to_generate)

    #deklarasi tanda yang mau digunakan
    tanda = "#"

    story = feature_to_generate.user_story #Dari database
    index = story.index(tanda) #5
    indexbr = 0
    for i in range ( index+1,len(story)): #KATA1
        if (story[i] == "#") :
            indexbr = i #10
            kata1 = story[index+1:indexbr] #kata1 dapat role
            for j in range ( indexbr+1,len(story)): #KATA2
                if (story[j] == "#") :
                    indexbr2 = j #24
                    for k in range ( indexbr2+1 , len(story)) :
                        if story[k] == "#" :
                            indexbr22 = k #30
                            kata2 = story[indexbr2+1:indexbr22] #kata2 dapat action
                            for l in range ( indexbr22+1 , len(story)) :#KATA3
                                if story[l] == "#" :
                                    indexbr3 = l #43
                                    for m in range ( indexbr3+1 , len(story)) :
                                        if story[m] == "#" :
                                            indexbr33 = m
                                            kata3 = story[indexbr3+1:indexbr33] #kata3 dapat benefit
                                            break
                                    break
                            break
                    break
            break
    
    #buat nama controller
    controllerName = feature_to_generate.feature_name+'Controller'

    #buat nama peran
    roleName = kata1

    #buat boundary kosong
    boundaryName = ""

    #mulai buat file .txt
    
    dirName = 'sequences'
    # Create target Directory if don't exist
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    else:    
        print("Directory " , dirName ,  " already exists")
        
    f = open('sequences/'+str(project_to_generate.project_name)+'_'+str(feature_to_generate.feature_name)+'_'+str(feature_id)+".txt","w")
    f.write("title "+feature_to_generate.feature_name+'\n')
    #f.write("@startuml\n")
    f.write("hide footbox\n")
    f.write('actor "'+roleName+'"\n')

    #looping khusus nyari scenario normal
    for (i, s) in enumerate(scenarios): 
        if(s.scenario_type == 'Normal'):
            #get condition sesuai scenario
            conditions = condition.objects.filter(scenario=s)

            #looping khusus nyari given karena given harus urutan pertama
            for (j, c) in enumerate(conditions):
                if(c.tipe == 'Given'):
                    given =  c.content
                    tanda = "#"
                    indexcond = given.index(tanda) 
                    indexcondbr = 0
                    for g in range ( indexcond+1,len(given)): #KATA1
                        if (given[g] == "#") :
                            indexcondbr = g 
                            boundaryName = given[indexcond+1:indexcondbr]
                            break
                        
                    f.write('boundary "'+boundaryName+'"\n')
                    f.write('control "'+controllerName+'"\n')

            #looping khusus when
            whenCount = 1
            for (j, c) in enumerate(conditions):
                
                if(c.tipe == 'When'):
                    message = ""
                    when = c.content
                    tanda = "#"
                    indexcond = when.index(tanda) 
                    indexcondbr = 0
                    for h in range ( indexcond+1,len(when)): #KATA1
                        if (when[h] == "#") :
                            indexcondbr = h 
                            message = when[indexcond+1:indexcondbr]
                            break

                    f.write('"'+roleName+'" --> "'+boundaryName+'" :'+message+'\n')
                      
                    if(whenCount == 1):
                        f.write('activate "'+boundaryName+'"\n')   

                    whenCount = whenCount + 1
                
                if(j == (len(conditions)-1)):
                    #ketika sudah sampai di terakhir, buat panah ke controller
                    f.write('"'+boundaryName+'" --> "'+controllerName+'" :empty\n')   
                    f.write('activate "'+controllerName+'"\n') 
            
            #looping khusus then
            if(len(scenarios) > 1):
                f.write('alt '+s.scenario_name+'\n')

            for (j, c) in enumerate(conditions): 
                if(c.tipe == 'Then'):
                    then = c.content
                    tanda = "#"
                    indexcond = then.index(tanda) 
                    indexcondbr = 0
                    for h in range ( indexcond+1,len(then)): #KATA1
                        if (then[h] == "#") :
                            indexcondbr = h
                            systemResponse = then[indexcond+1:indexcondbr]
                            break

                    f.write(' "'+controllerName+'" --> "'+boundaryName+'" :'+systemResponse+'\n')
                        
    #looping khusus nyari scenario alternative
    for (i, s) in enumerate(scenarios): 
        if(s.scenario_type == 'Alternative'):
            conditions = condition.objects.filter(scenario=s)

            if(len(scenarios) > 1):
                f.write('else '+s.scenario_name+'\n')

                #looping khusus then
                for (j, c) in enumerate(conditions): 
                    if(c.tipe == 'Then'):
                        then = c.content
                        tanda = "#"
                        indexcond = then.index(tanda) 
                        indexcondbr = 0
                        for h in range ( indexcond+1,len(then)): #KATA1
                            if (then[h] == "#") :
                                indexcondbr = h
                                systemResponse = then[indexcond+1:indexcondbr]
                                break

                        f.write(' "'+controllerName+'" --> "'+boundaryName+'" :'+systemResponse+'\n')

            if(i == (len(scenarios)-1)):
                #berarti scenario terakhir
                f.write('end\n')
                f.write('deactivate "'+boundaryName+'"\n')
    
    #f.write("@enduml\n")
    f = open('sequences/'+str(project_to_generate.project_name)+'_'+str(feature_to_generate.feature_name)+'_'+str(feature_id)+".txt","r")

    #generate sequence
    server = PlantUML(url='http://www.plantuml.com/plantuml/img/',
                          basic_auth={},
                          form_auth={}, http_opts={}, request_opts={})

    # Call the PlantUML server on the .txt file
    #downloads_path = str(Path.home() / "Downloads")

    server.processes_file(abspath(f'sequences/'+str(project_to_generate.project_name)+'_'+str(feature_to_generate.feature_name)+'_'+str(feature_id)+'.txt'))


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
