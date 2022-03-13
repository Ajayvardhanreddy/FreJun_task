from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('team/',  csrf_exempt(views.create_team), name='create_team'),
    path('availability/',  csrf_exempt(views.get_availability), name='get_availability'),
    path('task/',  csrf_exempt(views.task), name='create_task'),
    path('report/',  csrf_exempt(views.get_report), name='get_report'),
    path('login/', csrf_exempt(views.login), name='login'),
    path('logout/', csrf_exempt(views.logout), name='logout'),
]

