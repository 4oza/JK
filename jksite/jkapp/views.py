from django.shortcuts import render
from django.http import *
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .forms import UserForm

# Create your views here.
def index(request):
    userform = UserForm()
    # data = {"age": 70}
    # cat = ["Ноутбуки", "Принтеры", "Сканеры", "Диски", "Шнуры"]
    return TemplateResponse(request, "jkapp/index.html", {"form": userform})

def about(request):
    return TemplateResponse(request, 'jkapp/about.html')

def contact(request):
    return HttpResponse("<h2>Koнтaкты</h2>")

def products(request, productid):
    output = "<h2>Продукт № {0}</h2>".format(productid)
    return HttpResponse(output)

def users(request, id, name):
    output = "<h2>Пользователь</h2><h3>id: {0}  Имя: {1} </h3> ".format(id,name)
    return HttpResponse(output)

def products(request, productid = 1):
    output = "<h2>Продукт № {0}</h2>".format(productid)
    return HttpResponse(output)