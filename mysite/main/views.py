from django.shortcuts import render
from django.http import HttpResponse

from .models import ToDoList, Item
# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    # item = ls.item_set.get(id=1)
    # return HttpResponse("%s   <br><br> %s" %(ls.name, item.text))
    return render(response, "main/list.html", {"ls":ls})

def index2(response):
    return HttpResponse("more")

def home(response):
    return render(response, "main/home.html", {})
