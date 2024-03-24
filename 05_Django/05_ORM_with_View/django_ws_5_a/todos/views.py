from django.shortcuts import render
from .models import Todo

# Create your views here.
def index(request):
    todo = Todo.objects.all()
    # work = request.GET.get('work')
    context = {
        # 'work': work,
        'todo_list': todo,
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')

def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)