from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as dj_login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

def signup(request):
    return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def handlesignup(request):
    if request.method == 'POST':
        #get the parameters
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        #dept = request.POST['dropdownMenuLink']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        #check for errors in input
        if request.method == 'POST':
            try:
                user_exits = User.objects.get(username=request.POST['uname'])
                messages.error(
                    request, 'Id Number has already been registered. Make sure you have entered the correct ID Number'
                )
                return redirect('/signup')
            except User.DoesNotExist:
                if len(uname) > 15:
                    messages.error(
                        request, 'ID Number must be at most 6 characters. Please try again'
                    )
                    return redirect('/signup')

                if password1 != password2:
                    messages.error(
                        request, 'Password fields do not match. Please try again'
                    )
                    return redirect('signup')
                    

            #create the user
            user = User.objects.create_user(uname, email, password1)
            user.firtstname = fname
            user.last_name = lname
            user.save()

            messages.success(
                request, 'Your account has been successfully created'
            )
            return redirect('/')

        else:
            return HttpResponse('404 - NOT FOUND')

        
#view for rendering data from the login page
def handlelogin(request):
    if request.method == 'POST':
        #get the parameters
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(usernamme=name, password=password)

        #check for invalid login
        if user is not None:
            dj_login(request, user)
            messages.success(request, 'Successfully logged in' )
            return redirect('/')

        else:
            messages.error(request, 'Invalid Credentials, Please try again')
            return redirect('/')
    return HttpResponse('404 - NOT FOUND')

#view for rendering logout
def handlelogout(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('/')

