from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
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

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        # saves if valid fields are filled
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})
