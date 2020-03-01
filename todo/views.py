from django.shortcuts import render,redirect
from . models import TodoItem
from .forms import TodoForm
# Create your views here.

def home(request):
    todo = TodoItem.objects.all()
    return render(request,'todo/home.html',{'todos':todo})

def add(request):
    text = request.POST['text']
    a = TodoItem(text=text)
    a.save()
    return redirect('home')
def delete(request,num):
    text = TodoItem.objects.filter(id=num).delete()
    return redirect('home')

def update(request,num):
    text = TodoItem.objects.get(id=num)
    form = TodoForm(instance=text)
    if request.method== "POST":
        form = TodoForm(request.POST,instance=text)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request,'todo/update.html',{'form':form})