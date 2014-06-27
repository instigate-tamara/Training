from django.shortcuts import render
from django.http import HttpResponse
from appTraining.models import Lecturer,Group,Subject,Current,LectSubj,Student,GroupSubj,Log
import json

def Load(request):
    callback = request.GET.get('callback', '')
    groups = Group.objects.all()
    arrgroup = []
    for group in groups:
        namegroup = {
            'id': group.id,
            'groupNum': group.groupNum,
        }
        arrgroup.append(namegroup)
    response = json.dumps(arrgroup)
    response = callback + '(' + response + ');'
    return HttpResponse(response,content_type = "application/json");

def getListSubject(request):
    callback = request.GET.get('callback', '')   
    subjects = Subject.objects.get(id = 5)
    group = Group.objects.get(id = 1)
    currents = Current.objects.filter(subjectId = subjects.id)
    logs = Log.objects.filter(currentId = currents)
    students = Student.objects.filter(id = logs)
    student = []
    for cr in currents:
        roll = {
            'day' : str(cr.day),
            'student': [],
        }
        for log in logs:
            studMarks = {
                'id' : log.studId.id,
                'mark' : log.mark,
      #          'absence':log.absence,
            }
            roll['student'].append(studMarks)
        student.append(roll)       
    response = json.dumps(student)
    response = callback + '(' + response + ');'
    return HttpResponse(response,content_type = "application/json");

def getListGroup(request):
    callback = request.GET.get('callback', '')
    group = Group.objects.get(id = request.GET['groupid'])
    students = Student.objects.filter(groupId = group.id)
    subjects = GroupSubj.objects.filter(groupId = group.id)
    arrjson = []
    student = []
    subject = []
    sendInformation = {
        'student' : [],
        'subject' : []
    }
    for stud in students:
       studentData = {
            "id" : stud.id,
            'name' : stud.name,
            'surname' : stud.surname,
       }
       sendInformation["student"].append(studentData)
    
    for subj in subjects:
        subjectData = {
            'id' : subj.subjectId.id,
            'name' : subj.subjectId.name,
        }
        sendInformation["subject"].append(subjectData)
    student.append(sendInformation)
   # arrjson.append(stud)
    response = json.dumps(student) 
    response = callback + '(' + response + ');'
    return HttpResponse(response,content_type = "application/json");

def getListLecturer(request):
    callback = request.GET.get('callback', '')
    lecturers = Lecturer.objects.all()
    lecturer = [] 
    for lect in lecturers:
        response = {
            'name' : lect.name,
            'surname' : lect.surname,
            'email' : lect.email,
            'phoneNum' : lect.phoneNum,
        }
        lecturer.append(response)
        response = json.dumps(lecturer)
    response = callback + '(' + response + ');'
    return HttpResponse(response, content_type = "application/json");

def getListStudent(request):
    callback = request.GET.get('callback', '')
    students = Student.objects.all()
    student = [] 
    for stud in students:
        response = {
            'name' : stud.name,
            'surname' : stud.surname,
            'email' : stud.email,
            'phoneNum' : stud.phoneNum,
        }
        student.append(response)
        response = json.dumps(student)
    response = callback + '(' + response + ');'
    return HttpResponse(response, content_type = "application/json");

#def funcallback(request,response):
 #   callback = request.GET.get('callback', '')
  #  response = callback + '(' + response + ');'
