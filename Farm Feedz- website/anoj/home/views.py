from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "index.html")
    #return HttpResponse("Sanoj is a champ!")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip = request.POST.get("zip")
        contact=Contact(name=name,email=email,mobile=mobile,city=city,state=state,zip=zip,date=datetime.today())
        contact.save()
        messages.success(request, 'Your contact has been successful!')
    return render(request, "contact.html")

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
    # A backend authenticated the credentials
            return redirect("/")
        else:
            return render(request, 'login.html')
# No backend authenticated the credentials
    return render(request, 'login.html')
def logoutUser(request):
    logout(request)
    return render(request, 'login.html')

