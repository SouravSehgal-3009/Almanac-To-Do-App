from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    return render(request,'index.html')

def submit(request):
    obj = Task()
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority_level = request.GET['priority_level']
    obj.save()
    alltasks=Task.objects.all()
    paginator = Paginator(alltasks, 2) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return redirect('list')

def delete(request,id):
    obj = Task.objects.get(id=id)
    obj.delete()
    alltasks=Task.objects.all()
    paginator = Paginator(alltasks, 2) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return redirect('list')

def list(request):
    alltasks=Task.objects.all()
    paginator = Paginator(alltasks, 2) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'list.html',{'page_obj': page_obj})

def sortdata(request):
    alltasks=Task.objects.all().order_by('priority_level')
    paginator = Paginator(alltasks, 2) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'list.html',{'page_obj': page_obj})

def edit(request,id):
    obj = Task.objects.get(id=id)
    mydictionary = {
        "title" : obj.title,
        "description" : obj.description,
        "priority_level" : obj.priority_level,
        "id" : obj.id
    }
    return render(request,'edit.html',context=mydictionary)

def searchdata(request):
    q = request.GET['query']
    alltasks=Task.objects.filter(title__contains=q)
    paginator = Paginator(alltasks, 2) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'list.html',{'page_obj': page_obj})


def update(request,id):
    obj = Task(id=id)
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority_level = request.GET['priority_level']
    import datetime
    updated_time = datetime.datetime.now()
    obj.creation_time = updated_time
    obj.save()
    alltasks=Task.objects.all()
    paginator = Paginator(alltasks, 2) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return redirect('list')