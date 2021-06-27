"""Design URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Dar import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('darling',views.darling),
    path('ht/',views.htmltag),
    path('uname/<str:name>/',views.uname),
    path('unag/<str:un>/<int:ag>/',views.userage),
    path('stu/<str:sid>/<int:sage>/<str:sname>/',views.student),
    path('basic/',views.basic),
    path('sample/',views.sample),
    path('yt/<str:kname>/',views.ytname),
    path('pt/<int:id>/<str:sn>/',views.ptname),
    path('reddy/',views.reddy),
    path('emp/',views.employee),
    path('student/',views.student,name='student'),
    #path('studea/',views.studea,name='studea'),
    path('internalJS/',views.internalJS),
    path('register/',views.register,name='register'),
    path('dea/',views.deatiles,name='deatiles'),
    path('btsrp/',views.btfun),
    path('basicbt/',views.basicbt),
    path('kushala/',views.kushala,name='kushala'),
    path('btrg/',views.btrg,name="btrg"),
    path('newrg/',views.newrg,name="newrg"),
    path('update/<int:num>/',views.update,name='update'),
    path('Reg/',views.Reg,name
        ='Reg'),
    path('kushi/',views.kushi),
    path('display/',views.display,name="display"),
    path('viw/<int:y>/',views.viw,name="viw"),
    path('raju/',views.raju,name="raju"),
    path('rupdate/<int:x>',views.rupdate,name="rupdate"),
    path('Del/<int:s>/',views.Del,name="Del"),
    path('register2/', views.register2),
    path('display2/',views.display2,name='display2'),
    path('viw2/<int:num>/',views.viw2,name='viw2'),

 
 
]
