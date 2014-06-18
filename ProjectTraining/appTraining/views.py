from django.shortcuts import render
from django.http import HttpResponse
from appTraining.models import Lecturer,Group,Subject,Absence,Current,LectSubj,Log,Student,GroupSubj

def Load(request):
    response = HttpResponse()
    groups = Group.objects.all()
    gp = []
    for i in groups:
        gp.append(i.groupNum + "\n")
    response.content = gp
    return response;
#   return HttpResponse(request.GET['callback'] + "(" + gp + ");");

#def getListGroupSubj(request):

def getListSubject(request):
    response = HttpResponse()
    subjects = Subject.objects.get(id = 5)
    currents = Current.objects.filter(subjectId= subjects.id)
    logs = Log.objects.filter(currentId=currents)
    mark=[]
    day=[]
    for cr in currents:
        day.append(cr.day)
    for log in logs:
        mark.append(log.mark)
    response.content = str(day)+str(mark)+str(log.studId)
    return response;

def getListGroup(request):
    response = HttpResponse()
    group = Group.objects.get(id=9)
    students = Student.objects.filter(groupId = group.id)
    subjects = GroupSubj.objects.filter(groupId = group.id)
   # subjects1 = Subject.objects.filter(id = subjects.subjectId)
    stud=[]
    subj=[]
    for st in students:
        stud.append(st.name+st.surname)
    for sj in subjects:
        subj.append(sj.subjectId.name)
    response.content = str(stud)+str(subj)
    return response;
    #return HttpResponse(request.GET['callback'] + "(" + str(arrstud) + ");");


def getListLog(request):
    response = HttpResponse()
    marks = Log.objects.all().filter(mark = 7)
    mark = []
    for m in marks:
        mark.append(m.mark)
    response.content = str(mark)
    return response;

def getListSSMark(request):
    response = HttpResponse()
    subj = Log.objects.all().filter(studId = 10)
#    stud = Log.objects.all().filter(Current.objects.id = 8)
    r=Subject.objects.get(name="History")
    r1=Current.objects.filter(subjectId=r.id)
    r2=Log.objects.filter(currentId=r1)
#    r3=Absence.objects.filter(studId=r2.studId.id)
    marks = Log.objects.all()
    arrMark = []
    for i in r2: 
        arrMark.append(str(i.mark)+str(i.studId.name))
    response.content =str(arrMark)
    return response;

def getListLecturer(request):
    response = HttpResponse()
    lecturers = Lecturer.objects.all()
    l = []  
    for lect in lecturers:
        l.append(lect.name+"\n"+lect.surname+"\n")
    response.content = l
    return response;

