from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item, Processes
import subprocess
# Create your views here.

def index(response, id): 
    ls = ToDoList.objects.get(id=id)
    item = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1></br><p>%s</p>" %(ls.name, str(item.text)))



def get_processes(response):
    process_List = subprocess.call('powershell.exe Get-Process', shell=True)
    #Processes.objects.create(processList=process_List)
    #return HttpResponse( {{ print(process_List) }} )
    #return HttpResponse((subprocess.call('powershell.exe Get-Process', shell=True)))
    print(process_List)
    return render(response, "main/base.html")







