from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields, widgets
from blog.models import UserData
from django.contrib.auth import password_validation
from django.contrib.auth.models import User

class RegForm(forms.ModelForm):
    login = forms.CharField(required=True,label="login",widget= forms.TextInput(attrs={"class":'form-control'}))
    password1 = forms.CharField(required=True,label="parol",widget=forms.PasswordInput(attrs={"class":'form-control'}))
    password2 = forms.CharField(required=True,label="parolni takrorlang",widget= forms.PasswordInput(attrs={"class":'form-control'}))
    phone = forms.CharField(label="Telefon",widget= forms.TextInput(attrs={"class":'form-control'}))
    adress = forms.CharField(label="Manzil",widget= forms.TextInput(attrs={"class":'form-control'}))
    
    
    def clean_login(self):    
        login = self.cleaned_data['login'] 
        if User.objects.filter(username=login).exists():
        
            raise ValidationError("login band")
        return login
            
        
         
    def clean_password1(self):
        password1 = self.cleaned_data['password1']  
        if password1:
            password_validation.validate_password(password1)
            
        return password1
    
    def clean(self):
        super().clean()
        p1 = self.cleaned_data['password1']
        p2 = self.cleaned_data["password2"]
        if p1 and p2 and p1 != p2:
            raise ValidationError("parol mos emas")
        
    def save(self,commit=True):
        user = super().save(commit=False)
        login = self.cleaned_data['login'] 
        password1 = self.cleaned_data['password1'] 
        u = User.objects.create_user(username=login,password=password1)
        user.user = u
        if commit:
            user.save()
        return user
    class Meta:
        model = UserData
        fields = ("login","password1","password2","phone","adress")
         