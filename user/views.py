from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# class SignPost(View):
def sign(request):
    if request.method == "POST":
        login1 = request.POST['login']
        password = request.POST['password']
        print(login1)
        print(password)
        user = authenticate(request,username=login1,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect("blog:bosh")
    return render(request,"user/sign.html")
def post(self,request):
    return render(request,"user/sign.html")
    
class SignUp(View):
    
    
    def get(self,request):
        form = RegForm()
        return render (request,"user/signup.html",{"form":form})
    
    def post(self,request):
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            # x = form.save(commit = False)
            # x.user= request.user
            messages.add_message(request,messages.SUCCESS,"movaqiyatli ro'yhatdan otingiz ")            
            return redirect ("user:sign")
        else:
            return render(request,"user/signup.html",{"form":form})
        
@login_required(login_url="user:sign")        
def profil(request):
    
    return render(request,"user/profil.html")
 
class Change_password(View):
    def get(self,request):
        return render(request,"user/change_password.html")
    def post(self,request):
        old_password = request.POST["old_password"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        
        check = request.user.check_password(old_password)
        errors = 0
        if not check:
            messages.add_message(request,messages.WARNING,"Avvalgi parol noto'gri")
            errors +=1
        elif password1 != password2:
            messages.add_message(request,messages.WARNING,"Parollar mos emas")
            errors +=1
        if errors !=0:   
            return render(request,"user/change_password.html")
        else:
            request.user.set_password(password1)
            return redirect ('user:profil')
        

def logout_view(request):
    logout(request)
    return redirect('blog:bosh')