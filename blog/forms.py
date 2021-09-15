from django import forms
from django.forms import widgets
from django.forms.widgets import Select
from .models import *
from django.forms import modelform_factory
from django.core.exceptions import ValidationError


CommentForm = modelform_factory(Post,
                                 fields=('category','title','description'))
                                #  labels={'email':'Email','comment':'Izox'},
                                #  help_texts={"email":"Email manzilingizni kiritin"})




class ComForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('email','description')
        labels={'email':'Email','comment':'Izox'},
        help_texts={"email":"Email manzilingizni kiritin"}
        widgets={"email":forms.widgets.EmailInput(attrs={"class":"form-control"}),
                 'description':forms.widgets.Textarea(attrs={"class":"form-control"})
                 }
    
    



class CreatePostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),label='katologlar',widget=forms.widgets.Select(attrs={"size":1,"class":"form-control"}))
    class Meta:
        model = Post
        fields = ("category","title","tags","description","image")
        
        
        
    
class ContactForm(forms.Form):
    name = forms.CharField(label="ism", widget=forms.widgets.TextInput(attrs={"class":"form-control"}))
    surname = forms.CharField(label="familiya", widget=forms.widgets.TextInput(attrs={"class":"form-control"}))
    phone = forms.CharField(label="telefon", widget=forms.widgets.TextInput(attrs={"class":"form-control"}))
    msg = forms.CharField(label="Xabar matni", widget=forms.widgets.Textarea(attrs={"class":"form-control"}))
    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) < 3 or len(name) > 18:
            raise ValidationError("3 ta dan kam yoki 18 dan ko`p ")
        return name
    
    def clean_surname(self):
        surname = self.cleaned_data["surname"]
        if len(surname) < 3 or len(surname) > 18:
            raise ValidationError("3 ta dan kam yoki 18 dan ko`p ")
        return surname
    # def clean_phone(self):
    #     phone = self.cleaned_data["surname"]
    #     if len(phone) < 9 or len(phone) > 13:
    #         raise ValidationError("3 ta dan kam yoki 18 dan ko`p ")
    #     return phone
    
    def save(self):
        name = self.cleaned_data["name"]
        surname = self.cleaned_data["surname"]
        phone = self.cleaned_data["phone"]
        msg = self.cleaned_data["msg"]
        x = Contact.objects.create(name=name, surname=surname, phone=phone, msg=msg)
        return x
    
