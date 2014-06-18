from django.contrib import admin

# Register your models here.
from appTraining.models import Student,Lecturer,Subject,LectSubj,Group,Current,Log,Absence,GroupSubj
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','surname','groupId','phoneNum','email')
admin.site.register(Student,StudentAdmin)

class LecturerAdmin(admin.ModelAdmin):
    list_display = ('id','name','surname','phoneNum','email')
admin.site.register(Lecturer,LecturerAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id','name','hours')
admin.site.register(Subject,SubjectAdmin)

class LectSubjAdmin(admin.ModelAdmin):
    list_display = ('subjectId','lecturerId')
admin.site.register(LectSubj,LectSubjAdmin)

class GroupSubjAdmin(admin.ModelAdmin):
    list_display = ('groupId','subjectId')
admin.site.register(GroupSubj,GroupSubjAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('id','groupNum')
admin.site.register(Group,GroupAdmin)

class CurrentAdmin(admin.ModelAdmin):
    list_display = ('id','day','subjectId','lecturerId')
admin.site.register(Current,CurrentAdmin)

class LogAdmin(admin.ModelAdmin):
    list_display = ('mark','id','studId','currentId')
admin.site.register(Log,LogAdmin)

class AbsenceAdmin(admin.ModelAdmin):
    list_display = ('studId','absence')
admin.site.register(Absence, AbsenceAdmin)
