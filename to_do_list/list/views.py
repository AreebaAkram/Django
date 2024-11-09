from django.shortcuts import render, get_object_or_404, redirect
from .forms import taskform, dateform
from .models import task,date

def dates(request):
    success = False
    if request.method == 'POST':
        form= dateform(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form= dateform()
            data=date.objects.all()
    else:
        form= dateform()
        data=date.objects.all()
    return render (request, 'list/date.html', {'form': form, 'data': data, 'success': success})

def tasks(request):
    success = False
    if request.method == 'POST':
        form= taskform(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form= taskform()
            data=task.objects.all()
    else:
        form= taskform()
        data=task.objects.all()
    return render (request, 'list/task.html', {'form': form, 'data': data, 'success': success})


def update(request, id):
    instance=get_object_or_404(task, id=id)
    if request.method=='POST':
        form = taskform(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('task')
    else:
        form= taskform(instance=instance)

    return render(request, 'list/update.html', {'form':form})

def delete(request,id):
    instance= get_object_or_404(task, id=id)
    if request.method =='POST':
        instance.delete()
        return redirect('task')
    else:
        form= taskform(instance=instance)
    return render(request, 'list/delete.html', {'form':form})
