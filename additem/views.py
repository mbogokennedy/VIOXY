from django.shortcuts import render, redirect
from .models import additem
from .forms import additemForm

def available(request):
    additems = additem.objects.order_by('-date_added')
    context = {'additem': additems}
    return render(request, 'additem/available.html', context)

def post(request):
    if request.method == 'POST':
        form = additemForm(request.POST)
        if form.is_valid():
            new_addeditem = additem(business_name=request.POST['business_name'], description=request.POST['description'], email=request.POST['email'], contact=request.POST['contact'])
            new_addeditem.save()
            return redirect('available')
    else:        
        form = additemForm()
    context = {'form': form}
    return render(request, 'additem/post.html', context)

