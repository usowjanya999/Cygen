from django.shortcuts import render,redirect
from app1.models import register,Service
from django.contrib import messages
from django.db.utils import IntegrityError
# Create your views here.

def showIndex(request):
    return render(request,"index.html")

def emp_register(request):
    return render(request, "emp_register.html")

def save_register(request):
    na = request.POST.get("r1")
    no = request.POST.get("r2")
    em = request.POST.get("r3")


    try:
        register(name=na, empno=no, email=em).save()
        return redirect('emp_register')
    except IntegrityError:
        message = "User already registered"
        return render(request, "emp_register.html", {"error": message})




def emp_login(request):
    return render(request,"emp_login.html")

def login_check(request):
    un = request.POST.get("l1")
    return redirect('cygen_home')

    #data = register.objects.all()


    #for x in data:
        #if x==un:
            #return redirect('cygen_home')
        #else:
            #message = "Invalid User"
            #return render(request, "emp_login.html", {"error": message})





def cygen_home(request):
    return render(request,"cygen_home.html")

def cygen_add(request):
    return render(request,"cygen_add.html")

def save_service(request):
    na = request.POST.get("s1")
    des = request.POST.get("s2")
    pho = request.POST.get("s3")
    date = request.POST.get("s4")
    cust = request.POST.get("s5")
    Service(name=na,desc=des,Image=pho,Startdate=date,Customers=cust).save()

    return redirect("cygen_add")

def view_service(request):
    res=Service.objects.all()
    return render(request,"view_service.html",{"data":res})

def show_update(request):
    na = request.POST.get("s1")
    #query to read 1 record from db
    res = Service.objects.get(name=na)
    return render(request,"update.html",{"data1":res})

def update_ser(request):
    num=request.POST.get("u1")
    na = request.POST.get("u2")
    des = request.POST.get("u3")
    pho = request.POST.get("u4")
    start = request.POST.get("u5")
    cust = request.POST.get("u6")
    Service.objects.filter(name=na).update(no=num,desc=des,Startdate=start,customers=cust)
    return redirect('view_service')

def delete_emp(request):
    na = request.GET.get("na")
    Service.objects.filter(name=na).delete()

def emp_logout(request):

    return render(request,"emp_logout.html")