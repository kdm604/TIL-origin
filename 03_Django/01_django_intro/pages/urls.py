from django.urls import path
from . import views

urlpatterns = [

    path('static_example', views.static_example),
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('result/', views.result),
    path('art/', views.art),
    path('pong/', views.pong),
    path('ping/', views.ping),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('lotto/', views.lotto),
    path('ispal/<name>', views.ispal),
    path('isbirth/', views.isbirth),
    path('student/<str:name>', views.student),
    path('info/',views.info),
    path('template_language/', views.template_language),
    path('area/<int:r>', views.area),
    path('mul/<int:num1>/<int:num2>', views.mul),
    path('introduce2/<str:name>/<int:age>', views.introduce2),
    path('hello/<str:name>/<int:age>', views.hello),
    path('image/', views.image),
    path('dinner/', views.dinner),
    path('introduce/', views.introduce),
    path('index/', views.index),

]