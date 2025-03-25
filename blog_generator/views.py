from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login , logout
from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required (login_url="/login")
def index (request):
    return render (request , 'index.html')

#or i can you this to 

# def index(request):
#     if not request.user.is_authenticated:
#         return redirect("/login")
#     return render(request, "index.html")


def generate_blog(request):
     pass
     
def user_login(request):
    error_message = ""
    username = ""  
    password = ""



    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")  # Avoid KeyError
    
    if not username :
            error_message = "Username incarrect "
            return render(request, "login.html")
    
    if not password:
            error_message = "check your password it's incarrect "
            return render(request, "login.html")


    user = authenticate(request, username=username, password=password)
    if user is not None:
            login(request, user)
            return redirect("/")
    else:
            error_message = "Invalid username or password."
            return render(request, "login.html", {"error_message": error_message})

    return render(request, "login.html")


def user_signup (request):
    error_message = ""
    if request.method == 'POST':
        username = request.POST['username']
        email =  request.POST['email']
        createpassword =  request.POST['createpassword']
        confirmpassword =  request.POST['confirmpassword']
        
        
        if createpassword == confirmpassword:
            try:
                user = User.objects.create_user(username=username, email=email, password=createpassword)
                user.save()
                login(request,user)
                return redirect('/')
            except:
                error_message = 'Error creating acount ' 
                return render (request , 'signup.html' ,{'error_message':error_message})
        else:
            error_masssage = 'Password did not matched '
            return render(request , 'signup.html',{'error_message':error_message})

    return render (request, 'signup.html')

def user_logout (request):
    logout(request)
    return redirect('login')