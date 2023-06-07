from django.shortcuts import render,redirect,get_object_or_404
from .forms import TodoListForm
from django.http import HttpResponseRedirect,Http404,HttpResponse
from .models import TodoList

def home(request):
    todolists = TodoList.objects.all().order_by('-created_at')
    context = {'todolists':todolists}
    return render(request,'home.html',context)

def addTodoList(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return Http404('No form is invalid')
    form = TodoListForm()
    context = {'form':form}

    return render(request,'todo/add_item.html',context)

def editTodoList(request,pk):
    todolist = TodoList.objects.get(id=pk)
    if request.method == 'POST':
        form = TodoListForm(request.POST,instance=todolist)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = TodoListForm(instance=todolist,is_editing=True)
    context = {'form':form,'is_editing':True}
    return render(request,'todo/edit_item.html',context)


def deleteTodoList(request,pk):
    todolist = get_object_or_404(TodoList,id=pk)
    if request.method == 'POST':
        if 'confirm-delete' in request.POST:
            todolist.delete()
            return redirect('home')
        else:
            return redirect('home')
    
    context = {'todolist':todolist}
    return render(request,'todo/delete_item.html',context)


   
# def success(request):
#     return HttpResponse('<h5> Good Job you have succcessfull submitted a post</h5>')