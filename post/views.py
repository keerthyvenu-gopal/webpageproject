from django.shortcuts import render,redirect
from .models import post
from .forms import ModelForm
#create views here
def home(request):
    item=post.objects.all()
    return render(request,'home.html',{'items':item})
def post_view(request,post_id):
    item1=post.objects.get(id=post_id)
    return render(request,'post_view.html',{'item':item1})
def add_post(request):
    if request.method=='POST':
        title=request.POST.get('title')
        img=request.FILES['img']
        desc=request.POST.get('desc')
        p=post(title=title,img=img,desc=desc)
        p.save()
        print("post added")
        return redirect('/')

    return render(request,'add_post.html')

def update(request,id):
    obj=post.objects.get(id=id)
    form=ModelForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'obj':obj})

def delete(request,id):
    if request.method=="POST":
        obj=post.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')