from django.shortcuts import render,redirect
from .forms import *
from .models import *

def register(request):
    reg_form = RegistrationForm() 
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            print("Record Inserted!")
            return redirect('success_page')
        else:
            print(reg_form.errors)        
    else:
        reg_form = RegistrationForm()       
    return render(request, 'register.html', {'reg_form': reg_form})

def success_page(request):
    return render(request, 'success_page.html')

def login(request):
    error_message = None
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = UserProfile.objects.filter(username=username, password=password).first()
            if user:
                return redirect('dashboard') 
            else:
                error_message = "Invalid username or password. Please try again."
    else:
        form = UserLoginForm() 
    return render(request, 'login.html', {'form': form, 'error_message': error_message})

def dashboard(request):
    return render(request, 'dashboard.html')

def society_members(request):
    members = Member.objects.all()
    return render(request, 'society_members.html', {'members': members})

def society_watchmen(request):
    watchmen = Watchmen.objects.all()
    return render(request, 'society_watchmen.html', {'watchmen': watchmen})

def notice(request):
    notices = Notice.objects.all()
    return render(request, 'notice.html', {'notices': notices})

def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

def myprofile(request):
    userid = UserProfile.objects.all()
    return render(request, 'myprofile.html', {'userid': userid})
    
def deletedata(request,id):
    userid=UserProfile.objects.get(id=id)
    userid.delete()
    return redirect('dashboard')

def update(request,id):
    userid=UserProfile.objects.get(id=id)
    if request.method=='POST':
        updateuser=UserProfileForm(request.POST,instance=userid)
        if updateuser.is_valid():
            updateuser.save()
            print("Record Updated!")
            return redirect('myprofile')
        else:
            print(updateuser.errors)
    return render(request,'update.html',{'userid':userid})

def forgot_password(request):
    return render(request, 'forgot_password.html')