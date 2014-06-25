from django.shortcuts import render
from django.http import HttpResponse
from appTraining.models import Lecturer,Group,Subject,Absence,Current,LectSubj,Log,Student,GroupSubj
import json
def Load(request):
    callback = request.GET.get('callback', '')
    groups = Group.objects.all()
    arrgroup = []
    for group in groups:
        namegroup=({
            'id':group.id,
            'groupNum':group.groupNum,
        })
        arrgroup.append(namegroup)
    response = json.dumps(arrgroup)
    response = callback + '(' + response + ');'
    return HttpResponse(response)

def getListSubject(request):
    callback = request.GET.get('callback', '')   
    subjects = Subject.objects.get(id = 5)
    currents = Current.objects.filter(subjectId = subjects.id)
    logs     = Log.objects.filter(currentId = currents)
    students = Student.objects.filter(id = logs)
    absences = Absence.objects.filter(studId = students) 
    mark = []
    day = []
    ab = []
    stud = []

    for cr in currents:
        for log in logs:
           # for a in absences:
            abc=({
               'day':str(cr.day),
               'id':log.studId.id,
               'mark':log.mark,
            #        'absence':a.absence,
            })
            stud.append(abc)       
       # stud.append(day)
    response = json.dumps(stud)
    response = callback + '(' + response + ');'
    return HttpResponse(response,content_type="application/json");

def getListGroup(request):
    callback = request.GET.get('callback', '')
    group = Group.objects.get(id=request.GET['groupid'])
    students = Student.objects.filter(groupId = group.id)
    subjects = GroupSubj.objects.filter(groupId = group.id)
    arrjson = []
    stud=[]
    subj=[]
    t=[]
    #$t.append('student')
    for st in students:
        response = {
            'id' : st.id,
            'name' : st.name,
            'surname' : st.surname,
        }
        stud.append(response)
    for sj in subjects:
        response1 = {
            'id' : sj.subjectId.id,
            'name' : sj.subjectId.name,
        }
        subj.append(response1)
    t.append(subj) 
    arrjson.append(subj)
    arrjson.append(stud)
    response = json.dumps(json) 
    response = callback + '(' + response + ');'
    return HttpResponse(response,content_type="application/json");

def getListLecturer(request):
    callback = request.GET.get('callback', '')
    lecturers = Lecturer.objects.all()
    lect =[] 
    for lt in lecturers:
        response = ({
            'name' : lt.name,
            'surname' : lt.surname,
            'email' : lt.email,
            'phoneNum' : lt.phoneNum,
        })
        lect.append(response)
        response = json.dumps(lect)
    response = callback + '(' + response + ');'
    return HttpResponse(response, content_type="application/json");

def getListStudent(request):
    callback = request.GET.get('callback', '')
    students = Student.objects.all()
    stud = [] 
    for st in students:
        response = ({
            'name' : st.name,
            'surname' : st.surname,
            'email' : st.email,
            'phoneNum' : st.phoneNum,
        })
        stud.append(response)
        response = json.dumps(stud)
    response = callback + '(' + response + ');'
    return HttpResponse(response, content_type="application/json");
#def funcallback(request,response):
 #   callback = request.GET.get('callback', '')
  #  response = callback + '(' + response + ');'
