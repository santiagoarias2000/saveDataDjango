"""django_parcial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path
import json


def list_marvel(request):
    characters = {"heroe" : [{"name": "Spiderman","description": "This is a boy","image": "https://img.europapress.es/fotoweb/fotonoticia_20190710171535_1200.jpg"},{"name": "Vision","description": "This is a boy","image": "https://img.europapress.es/fotoweb/fotonoticia_20151209145712_1280.jpg"}]}

    html = '<h1>hello new heroes</h1> '+str(request.POST['name'])+'<h2>Your description</h2>'+str(request.POST['description'])+'<h3>imagen</h3>'+str(request.POST['imagen'])
    for character in characters['heroe']:
        html += '<h2 color: red>{}</h2> <p>{}</p><img src="{}"/>'.format(character['name'], character['description'], character['image'])
    return HttpResponse(html)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('characters/', list_marvel),
]
