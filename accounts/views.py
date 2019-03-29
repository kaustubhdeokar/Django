from django.shortcuts import render , HttpResponse
# Create your views here.

def home(request):
    num=list(range(1,10))
    name='kaustubh deokar'
    dic={
        'numbers':num,
        'name':name,
    }
    return render(request,'accounts/home.html',dic)

def login(request):
    return render(request,'accounts/login.html',{})

def logout(request):
    return render(request,'accounts/logout.html',{})
    