
from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("Django running with Docker Compose + Postgres!")

urlpatterns=[ path("",home) ]
