
from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth.models import User,auth

# Create your views here.
def MUSIC(request):
    return render(request,'blur.html')

def sig(request):
    if request.method == "POST" :
        fname = request.POST['firstname']
        email = request.POST['email']

        uname = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username=uname,email=email,password=password,first_name=fname)
        print("account created successfully "+uname)
        return redirect('/')
    else:
        return render(request, 'sig.html')

def log(request):
    if request.method == "POST" :
        uname = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=uname,password=password)

        if user is not None:
            auth.login(request,user)
            print("logged in")
            return HttpResponse("Redirecting......")
        else:
            print("Invalid username or password")
            return redirect('log.html')
            

    else:
        return render(request, 'log.html')



def home(request):
    return render(request,'index.html')


