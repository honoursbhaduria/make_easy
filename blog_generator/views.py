from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login , logout
from django.shortcuts import render ,redirect

# Create your views here.

def index (request):
    return render (request , 'index.html')


def user_login(request):
    if request.method == 'POST' :
        username = request.POST['username']
        createpassword =  request.POST['createpassword']

        user = authenticate(request , username=username , password = createpassword)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html',{'error_message'})

    return render (request , 'login.html')

def user_signup (request):

    if request.method == 'POST':
        username = request.POST['username']
        email =  request.POST['email']
        createpassword =  request.POST['createpassword']
        confirmpassword =  request.POST['confirmpassword']
        
        
        if createpassword == confirmpassword:
            try:
                user = User.objects.create_user(username,email,createpassword)
                user.save()
                login(request,user)
                return redirect('/')
            except:
                error_message = 'Error creating acount ' 
                return render (request , 'signup.html' ,{'error_masssage':error_masssage})
        else:
            error_masssage = 'Password Did not matched '
            return render(request , 'signup.html',{'error_masssage':error_masssage})

    return render (request, 'signup.html')

def user_logout (request):
    pass