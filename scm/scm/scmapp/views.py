import datetime
import random
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from .models import User,Book_ground,Admin,Event

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def user_reg(request):
    return render(request,'user_reg.html')

def user_test(request):
    if request.method=="POST":
        name=request.POST.get('uname')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        password=request.POST.get('password')
        contact=request.POST.get('contact')
        record=User(name=name,email=email,gender=gender,password=password,contact=contact)
        record.save()
        return render(request,'user_login.html')

def user_login(request):
    if 'u_name'in request.session:
        param={'name':request.session.get('u_name')}
        return render(request,'userhome.html',param)
    return render(request,'user_login.html')

def user_check(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        try:
            user=User.objects.get(name=uname)
            if user.password==password:
                request.session['u_name']=uname
                return userhome(request)
            else:
                param={'msg':"Password doesn't match..!"}
                return render(request,'user_login.html',param)
        except Exception as e:
            param={'msg':'Username does not exist..!'}
            return render(request,'user_login.html',param)



def userhome(request):
    if 'u_name' in request.session:
        uname=request.session.get('u_name')
        param={'name':uname}
        return render(request,'userhome.html',param)
    else:
        param={"status":'you need to login'}
        return render(request,'user_login.html',param)

def admin_login(request):
    return render(request,'admin_login.html')

def ground_booking(request):
    if 'u_name'  in request.session:
        param={'date':datetime.date.today}
        return render(request,'ground_booking.html',param)
    else:
        param={'status':'you need to login'}
        return render(request,'user_reg.html',param)

def data_ground_booking(request):
    if request.method=="POST":
        date=request.POST.get("date")
        time=request.POST.get("time")
        try:
            book=Book_ground.objects.get(date=date)
            param={'status':"Please select other date"}
            return render(request,'ground_booking.html',param)
        except Exception as e:
            user=User.objects.get(name=request.session.get('u_name'))
            book=Book_ground(uid=user.uid,name=user.name,date=date,time=time,mobile=user.contact)
            book.save()
            param={'status':"Booked successfully..!"}
            return render(request,'userhome.html',param)
    else:
           param={'msg':'Something went wrong'}
           return render(request,'ground_booking.html',param)

def admin_login_page(request):
    if "a_name" in request.session:
        param={'name':request.session.get("a_name")}
        return render(request,'adminhome.html',param)
    return render(request,'admin_login.html')

def admin_check(request):
    if request.method=="POST":
        aname=request.POST.get('aname')
        password=request.POST.get('password')
        try:
            ad=Admin.objects.get(name=aname)
            if ad.password==password:
                request.session['a_name']=aname
                return adminhome(request)
            else:
                param={'msg':"Password doesn't match..!"}
                return render(request,'admin_login.html',param)
        except Exception as e:
            param={'msg':'Username does not exist..!'}
            return render(request,'admin_login.html',param)

def adminhome(request):
    if 'a_name' in request.session:
        aname=request.session.get('a_name')
        param={'name':aname}
        return render(request,'adminhome.html',param)
    else:
        param = {"status": 'you need to login'}
        return render(request, 'admin_login.html', param)

def admin_booking(request):
    if 'a_name' in request.session:
        booking=Book_ground.objects.all()
        param={'data':booking}
        return render(request,'admin_booking.html',param)
    else:
        param={'status':"You need to login"}
        return render(request,'admin_login.html')

def admin_event(request):
    if 'a_name' in request.session:
        event=Event.objects.all()
        param={'data':event}
        return render(request,'admin_event.html',param)
    else:
        param={'status':"You need to login"}
        return render(request,'admin_login.html',param)

def add_event(request):
    if 'a_name' in request.session:
        param={'date':datetime.date.today}
        return render(request,'add_event.html',param)
    else:
        param={'status':'You need to login'}
        return render(request,'admin_login.html',param)

def db_add_event(request):
    if request.method=="POST":
        ename=request.POST.get('ename')
        edate=request.POST.get('edate')
        etime=request.POST.get('etime')
        eduration=request.POST.get('eduration')
        event=Event(name=ename,date=edate,time=etime,duration=eduration)
        event.save()
        # request.session['event_status']='Event added successfully..'
        return admin_event(request)
    else:
        return admin_event(request)

def admin_logout(request):
    if 'a_name' in request.session:
        del request.session['a_name']
        return render(request,'admin_login.html')
    else:
        param={'status':'You need to login'}
        return render(request,'admin_login.html',param)

def user_logout(request):
    if 'u_name' in request.session:
        del request.session['u_name']
        return render(request,'user_login.html')
    else:
        param={'status':'You need to login'}
        return render(request,'user_login.html',param)

def show_event(request):
    if 'u_name' in request.session:
        event=Event.objects.all()
        param={'data':event}
        return render(request,'show_event.html',param)
    else:
        param={'status':'You need to login'}
        return render(request,'user_login.html',param)

def event_delete(request):
    if 'a_name' in request.session:
        id=request.GET.get('eid')
        Event.objects.filter(eid=id).delete()
        return admin_event(request)
    else:
        param={'status':'You need to login.'}
        return render(request,'admin_login.html',param)

def mail_send(request):
    return render(request,'email_form.html')

def email_check(request):
    email=request.POST.get('email')
    subject='Forget Password'
    otp=random.randint(1000,9999)
    msg='OTP :'
    msg+=msg+str(otp)
    to=(email,)
    email_from=settings.EMAIL_HOST_USER
    send_mail(subject,msg,email_from,to,otp)
    param={'otp':otp,'email':email}
    return render(request,'enter_otp.html',param)

def otp_check(request):
    emailid=request.POST.get('emailid')
    myotp=request.POST.get('myotp')
    otp=request.POST.get('otp')
    if(myotp==otp):
        param={'email':emailid}
        return render(request,'update_pass.html',param)
    else:
        param={'otp':myotp,'msg':'Entered Wrong OTP !','email':emailid}
        return render(request,'enter_otp.html',param)

def update_pass(request):
    password=request.POST.get('pass')
    myemail=request.POST.get('emailid')
    user=User.objects.get(email=myemail)
    user.password=password
    user.save()
    return render(request,'user_login.html')

