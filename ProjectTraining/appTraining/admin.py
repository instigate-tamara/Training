from django.contrib import admin

# Register your models here.
from appTraining.models import Student,Lecturer,Subject,LectSubj,Group,Current,GroupSubj,Log
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','surname','getGroupNum','phoneNum','email')    
    def getGroupNum(self, obj):
       return obj.groupId.groupNum
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
    list_display = ('getGroupNum','getSubjectName')
    def getGroupNum(self, obj):
       return obj.groupId.groupNum
    def getSubjectName(self, obj):
       return obj.subjectId.id
admin.site.register(GroupSubj,GroupSubjAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('id','groupNum')
admin.site.register(Group,GroupAdmin)

class CurrentAdmin(admin.ModelAdmin):
    list_display = ('id','day','getSubjectName','lecturerId')
    def getSubjectName(self, obj):
       return obj.subjectId.id

admin.site.register(Current,CurrentAdmin)

class LogAdmin(admin.ModelAdmin):
    list_display = ('id','mark','getStudentName','getCurrentDay','absence')
    def getStudentName(self, obj):
       return obj.studId.name
    def getCurrentDay(self, obj):
       return obj.currentId.day
admin.site.register(Log,LogAdmin)

