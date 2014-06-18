from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ProjectTraining.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^training/lecturer$','appTraining.views.getListLecturer'),
    url(r'^training$','appTraining.views.Load'),
    url(r'^training/group$','appTraining.views.getListGroup'),
    url(r'^training/mark$','appTraining.views.getListLog'),
    url(r'^training/ssmark$','appTraining.views.getListSSMark'),
    url(r'^training/subject','appTraining.views.getListSubject')



)

