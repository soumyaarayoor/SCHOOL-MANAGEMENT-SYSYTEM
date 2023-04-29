from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from myapp.forms import CustomUserCreationForm


# Create your views here.
def home(request):
    return render(request,'home.html')
def studenthome(request):
    return render(request,'studenthome.html')

def teacherhome(request):
    return render(request,'teacherhome.html')

def adminhome(request):
    return render(request, 'adminhome.html')
def signup(request):

    return render(request,'signup.html')
def admin_page(request):
    return redirect('/admin/')
def studentsignup(request):

    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.is_teacher = True
            f.save()
            return home(request)
    return render(request, 'studentsignup.html', {'form': form})
def teachersignup(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.is_teacher = True
            f.save()
            return home(request)
    return render(request, 'teachersignup.html', {'form': form})
def studentlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)

        if user and user.is_student == True:
            login(request, user)
            return studenthome(request)

        else:
            return studenthome(request)

    return render(request, 'studentlogin.html')
def teacherlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)

        if user and user.is_student == True:
            login(request, user)
            return teacherhome(request)

        else:
            return teacherhome(request)


    return render(request,'teacherlogin.html')
def logout(request):

    return render(request,'home.html')


