from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import TodoItem
from .forms import TodoForm


def index(request):
    todoList = TodoItem.objects.order_by('id')
    form = TodoForm()
    context = {'todoList': todoList, 'form': form}
    return render(request, 'todo/index.html', context)


@require_POST
def add(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        newitem = TodoItem(text=request.POST['text'])
        newitem.save()

    return redirect('index')


def delete(request, id):
    item = TodoItem.objects.get(id=id)
    item.delete()
    return redirect('index')


def deleteall(request):
    TodoItem.objects.all().delete()
    return redirect('index')


def checkoff(request, id):
    item = TodoItem.objects.get(id=id)
    item.completed = True
    item.save()
    return redirect('index')


def uncheck(request, id):
    item = TodoItem.objects.get(id=id)
    item.completed = False
    item.save()
    return redirect('index')
