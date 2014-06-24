from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ProjectTraining.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^training/lecturer$','appTraining.views.getListLecturer'), #dacaxosnri masin informacia 
    url(r'^training$','appTraining.views.Load'),       #Stanal xmberi anunnery
    url(r'^training/group$','appTraining.views.getListGroup'),   # Stanal xmbi matyan@
    url(r'^training/subject','appTraining.views.getListSubject'), #Trvac ararkayic 
    url(r'^training/student$','appTraining.views.getListStudent'), #usanoxneri masin informacia
#   url(r'^training/uniqueStudent$','appTraining.views.UniqueStud')


)

