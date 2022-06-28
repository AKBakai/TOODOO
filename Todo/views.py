from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
from django.views.decorators.http import require_POST


def index(request):
    todo = Todo.objects.order_by('id')
    form = TodoForm()
    context = {'todo_list': todo, 'form': form}
    return render(request, 'index.html', context)


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()
    return redirect('/')


def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    if todo.complete:
        todo.complete = False
        todo.save()
    else:
        todo.complete = True
        todo.save()
    return redirect('/')


def deleteCompleted(request):
    Todo.objects.filter(complete=True).delete()
    return redirect('index')


def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')