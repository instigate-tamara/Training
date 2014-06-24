from django.db import models

# Create your models here.
class Lecturer(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 15)
    surname = models.CharField(max_length = 20)
    phoneNum = models.CharField(max_length = 15)
    email = models.EmailField(max_length = 30)
   
class Subject(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 15)
    hours = models.IntegerField(default = 0)
   
class LectSubj(models.Model):
    subjectId = models.ForeignKey(Subject)
    lecturerId = models.ForeignKey(Lecturer)

class Group(models.Model):
    id = models.AutoField(primary_key = True)
    groupNum = models.CharField(max_length = 10)
   

class GroupSubj(models.Model):
    groupId = models.ForeignKey(Group)
    subjectId = models.ForeignKey(Subject)

class Student(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 15)
    surname = models.CharField(max_length = 20)
    groupId = models.ForeignKey(Group)
    phoneNum = models.CharField(max_length = 15)
    email = models.EmailField(max_length = 30)

#class Auditorium(models.Model):
 #   id = models.AutoField(primary_key = True)
  #  auditNum = models.CharField(max_length = 10)
   # employment = models.BooleanField(default = True)

class Current(models.Model):
    id = models.AutoField(primary_key = True)
    day = models.DateField('date published')
   # auditId = models.ForeignKey(Auditorium)
    subjectId = models.ForeignKey(Subject)
    lecturerId = models.ForeignKey(Lecturer)

class Log(models.Model):
    mark = models.IntegerField(default = 0)
    studId = models.ForeignKey(Student)
    currentId = models.ForeignKey(Current)

class Absence(models.Model):
    studId = models.ForeignKey(Student)
    absence = models.BooleanField(default = False)


