from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .models import Employee,Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(request):
    return render(request,'blog/home.html')
def about(request):
    return render(request,'blog/about.html')
def contact(request):
    return render(request,'blog/contact.html')

def reg(request):
    return render(request,'blog/reg.html')

def getform(request):
    btn=request.GET.get('sub')
    if btn=='Insert':
        name=request.GET.get('ename')
        loc=request.GET.get('eloc')
        sal=request.GET.get('esal')
        data=Employee(ename=name,eloc=loc,esal=sal)
        data.save()
        param={'msg':'Data submitted Successfully...'}
        return render(request,'blog/reg.html',param)
    if btn=='Display':
        record=Employee.objects.all()
        param={'data':record}
        return render (request,'blog/reg.html',param)


def more(request):
    return render(request,'blog/more.html')

def moredata(request):
    btn=request.GET.get('sub')
    if btn=='Display':
        name=request.GET.get('ename')
        record=Employee.objects.get(ename=name)
        param={'data':record}
        return render(request,'blog/more.html',param)
    if btn=='Delete':
        name=request.GET.get('ename')
        Employee.objects.filter(ename=name).delete()
        param={'msg':'Record deleted successfully...!!'}
        return render(request,'blog/more.html',param)
    if btn=="Edit":
        name=request.GET.get('ename')
        record=Employee.objects.get(ename=name)
        param={'data':record}
        return render(request,'blog/edit.html',param)

def more_update(request):
    name=request.GET.get('ename')
    loc=request.GET.get('eloc')
    sal=request.GET.get('esal')
    data=Employee.objects.get(ename=name)
    data.eloc=loc
    data.esal=sal
    data.save()
    param={'msg':'Record updated Successfully...!!'}
    return render(request,'blog/more.html',param)



def action(request):
    name=request.GET.get('ename')
    Employee.objects.filter(ename=name).delete()
    param={'msg':'Record deleted successfully...!!'}
    return render(request,'blog/reg.html',param)

def edit(request):
    name=request.GET.get('name')   #why name and not ename?
    record = Employee.objects.get(ename=name)
    param = {'data': record}
    return render(request, 'blog/edit.html', param)


def upload_product(request):
    return render (request,'blog/upload_product.html')

def uploaddata(request):
    btn=request.POST.get('sub')
    if btn=='Insert':
        prod=Product()
        prod.product_name=request.POST.get('pname')
        prod.product_cat=request.POST.get('pcat')
        prod.product_subcat=request.POST.get('pscat')
        prod.product_price=request.POST.get('pprice')
        prod.product_date=request.POST.get('pdate')
        if len(request.FILES)!=0:
            prod.product_image=request.FILES['pimg']
        prod.save()
        param={'msg':"file uploaded successfully..."}
        return render(request,'blog/upload_product.html',param)
    if btn=='Display':
        record=Product.objects.all()
        param={'data':record}
        return render(request,'blog/upload_product.html',param)


def signup(request):
    return render(request,'blog/reguser.html')

def reguser(request):
    username=request.GET.get('uname')
    email=request.GET.get('email')
    password=request.GET.get('password')
    myuser=User.objects.create_user(username,email,password)
    myuser.save()
    param={'msg':'Registered successfully....!!'}
    return render(request,'blog/reguser.html',param)




def loginform(request):
    return render(request,'blog/loginform.html')

def loginuser(request):
    uname=request.GET.get('uname')
    password=request.GET.get('password')
    user=authenticate(username=uname,password=password)
    if user is not None:
        login(request,user)
        return render(request,'blog/home.html')
    else:
        param={'msg':'username or password is incorrect'}
        return render(request,'blog/loginform.html',param)

def logoutuser(request):
    logout(request)
    return redirect('loginform')



def ajax(request):
    return render(request,'blog/ajax.html')

def create(request):
    ename=request.POST.get('ename')
    eloc=request.POST.get('eloc')
    esal=request.POST.get('esal')
    data=Employee(ename=ename,eloc=eloc,esal=esal)
    data.save()
    return render(request,'blog/ajax.html')


def show(request):
    record=list(Employee.objects.all().values())
    data=dict()
    data['dt']=record
    return JsonResponse(data)

def delete(request):
    eid=request.GET.get('id')
    Employee.objects.filter(id=eid).delete()
    return render(request,'blog/ajax.html')