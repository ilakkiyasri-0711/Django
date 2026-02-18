from django.shortcuts import render,HttpResponse,redirect
from .models import *
def homepage(request):
    # return HttpResponse("welcome")
    return render(request,'home.html')
def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        reg  = request.POST.get('reg')
        college = request.POST.get('college')
        sub1 = request.POST.get('sub1')
        sub2 =request.POST.get('sub2')
        sub3 =request.POST.get('sub3')
        sub4 =request.POST.get('sub4')
        print(name,reg,college,sub1,sub2,sub3,sub4)
        obj=Reg()
        obj.name=name
        obj.reg=reg
        obj.college=college
        obj.sub1=sub1   
        obj.sub2=sub2 
        obj.sub3=sub3
        obj.sub4=sub4
        obj.save()
        return redirect('login')
        return HttpResponse("Registered successfully")
    return render(request,'register.html')
def login (request):
    if request.method == "POST":
        name=request.POST.get('username')
        reg=request.POST.get('reg')
        print(name,reg)
        re=Reg.objects.get(name=name)
        print("Login here...")
        if re.reg ==int(reg):
            return redirect('table')
            # return HttpResponse("login sucessfully")
        else:
            return redirect('login')
    return render(request,"login.html")

def table(request):
    data=Reg.objects.all()
    return render(request,"table.html",{'q':data})


def delete(request,id):
    r=Reg.objects.get(id=id)
    r.delete()
    
    return redirect('table')

def update(request,id):
    da=Reg.objects.get(id=id)
    return render(request,"update.html",{'data':da}) 
   

def update_all(request):
    if request.method == "POST":
        name = request.POST.get('name')
        reg  = request.POST.get('reg')
        college = request.POST.get('college')
        sub1 = request.POST.get('sub1')
        sub2 =request.POST.get('sub2')
        sub3 =request.POST.get('sub3')
        sub4 =request.POST.get('sub4')
        print(name,reg,college,sub1,sub2,sub3,sub4)
        obj=Reg.objects.get(id=id)
        obj.name=name
        obj.reg=reg
        obj.college=college
        obj.sub1=sub1   
        obj.sub2=sub2 
        obj.sub3=sub3
        obj.sub4=sub4
        obj.save()
        return redirect('table')



# Create your views here.

