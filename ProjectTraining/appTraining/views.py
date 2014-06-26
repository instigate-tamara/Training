from django.shortcuts import render
from django.http import HttpResponse
from appTraining.models import Lecturer,Group,Subject,Current,LectSubj,Student,GroupSubj,Log
import json
def Load(request):
#    callback = request.GET.get('callback', '')
    groups = Group.objects.all()
    arrgroup = []
    for group in groups:
        namegroup={
            'id':group.id,
            'groupNum':group.groupNum,
        }
        arrgroup.append(namegroup)
    response1 = json.dumps(arrgroup)
    response =  response1 
    return HttpResponse(response)

def getListSubject(request):
    callback = request.GET.get('callback', '')   
    subjects = Subject.objects.get(id = 5)
    currents = Current.objects.filter(subjectId = subjects.id)
    logs = Log.objects.filter(currentId = currents)
    students = Student.objects.filter(id = logs)
    stud = []
    for cr in currents:
        for log in logs:
            abc={
                'day':str(cr.day),
                'id':log.studId.id,
                'mark':log.mark,
      #          'absence':log.absence,
            }
            stud.append(abc)       
    response = json.dumps(stud)
    response = callback + '(' + response + ');'
    httpResponse = HttpResponse();
    httpResponse.content = response;
    return httpResponse;
def getListGroup(request):
    return HttpResponse(response,content_type="application/json");
    callback = request.GET.get('callback', '')
    group = Group.objects.get(id=request.GET['groupid'])
    students = Student.objects.filter(groupId = group.id)
    subjects = GroupSubj.objects.filter(groupId = group.id)
    arrjson = []
    stud=[]
    subj=[]
    sendInformation = {
        'student':[],
        'subject':[]
    }
    for st in students:
       studData = {
            "id" :  st.id,
            'name' :  st.name,
            'surname' :  st.surname,
       }
       sendInformation["student"].append(studData)
    
    for sj in subjects:
        subjData = {
            'id' : sj.subjectId.id,
            'name' : sj.subjectId.name,
        }
        sendInformation["subject"].append(subjData)
    stud.append(sendInformation)
    arrjson.append(stud)
    response = json.dumps(arrjson) 
    response = callback + '(' + response + ');'
    return HttpResponse(response,content_type="application/json");

def getListLecturer(request):
    callback = request.GET.get('callback', '')
    lecturers = Lecturer.objects.all()
    lect =[] 
    for lt in lecturers:
        response = {
            'name' : lt.name,
            'surname' : lt.surname,
            'email' : lt.email,
            'phoneNum' : lt.phoneNum,
        }
        lect.append(response)
        response = json.dumps(lect)
    response = callback + '(' + response + ');'
    return HttpResponse(response, content_type="application/json");

def getListStudent(request):
    callback = request.GET.get('callback', '')
    students = Student.objects.all()
    stud = [] 
    for st in students:
        response = {
            'name' : st.name,
            'surname' : st.surname,
            'email' : st.email,
            'phoneNum' : st.phoneNum,
        }
        stud.append(response)
        response = json.dumps(stud)
    response = callback + '(' + response + ');'
    return HttpResponse(response, content_type="application/json");
#def funcallback(request,response):
 #   callback = request.GET.get('callback', '')
  #  response = callback + '(' + response + ');'
