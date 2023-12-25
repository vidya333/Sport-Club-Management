from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("<h1> Welcome to home page</h1> <a href='home'>Home</a>|<a href='about'>About</a>|<a href='contact'>Contact</a>")
    return render(request, 'test/home.html')
def aboutus(request):
    #return HttpResponse("<h1>Welcome this is About us page</h1><a href='home'>Home</a>|<a href='about'>About</a>|<a href='contact'>Contact</a>")
    return render(request,"test/about.html")
def contact(request):
    #return HttpResponse("<h1> Welcome This is Contact Page</h1><a href='home'>Home</a>|<a href='about'>About</a>|<a href='contact'>Contact</a>|<a href='test'>Test</a>")
    return render(request,"test/contact.html")
def test(request):
    #return HttpResponse("<h1>This is test Function</h1>")
    return render(request,'test/test.html')