from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .forms import RegistrationForm,LoginForm
from .models import Student
def index(request):
    return render(request,'pages/home.html')
def student(request):
    return render(request,'pages/student.html')
def teacher(request):
    return render(request,'pages/teacher.html')
def reg(request):
    form= RegistrationForm()
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            user = form.cleaned_data['username']
            password = form.cleaned_data['password']
            data = Student.objects.all()
            for s in data:
                if s.username == user:
                    return render(request,'pages/fail.html')
            form.save()
            return render(request,'pages/sucess.html')
    return render(request,'pages/register.html',{'form':form})
def login(request):
    form= LoginForm()
    if request.method == 'POST':
        form= LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            password = form.cleaned_data['password']
            data = Student.objects.all()
            for s in data:
                if s.username == user and s.password == password:
                    return render(request,'pages/student.html')
            return render(request,'pages/fail1.html')
    return render(request,'pages/login.html',{'form': form})