# from blog.help import paginate_generator
from django.shortcuts import render,redirect,get_object_or_404,\
get_list_or_404
from .forms import *
from django.contrib import messages
from django.views.decorators.http import*
from django.http import HttpResponse,HttpResponseRedirect,\
FileResponse,JsonResponse
from .models import *
from .forms import CommentForm, CreatePostForm
from django.db.models import F,Q,Min,Max,Count
from django.template.loader import get_template,render_to_string
from django.urls import reverse,reverse_lazy
from django.views.generic import View,CreateView
from django.views.generic.edit import UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.dates import MonthArchiveView,DateDetailView
from django.views.generic.dates import DayArchiveView
import random
from django.core.paginator import Paginator

import datetime

class IndexView(TemplateView):
	template_name = "index.html"

	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(*args,**kwargs)
		context["categorys"] = Category.objects.all()
		p = Post.objects.all()
		context["posts"] = p[:25]
		context["teg"] = Tag.objects.all()
		return context

def get_url(request):
	if "p" in request.get:
		print(request.GET.get("p"))
		print("okk")
	else:
		print("error")


class CategoryPostsView(View):

	def get(self,request,category_slug):
		#category = get_list_or_404(Category,id=category_id)
		try:
			category = Category.objects.get(slug=category_slug)
		except:
			return render(request,"404.html")
		posts = category.postlar.all()
		paginator = Paginator(posts,5,orphans=0,allow_empty_first_page=True)
		if "page" in request.GET:
			page_num = request.GET['page']
		else:
			page_num = 1
		page = paginator.get_page(page_num)
		c = {"posts": page.object_list, "page": page, "category": category}



		return render(request,"category/category_posts.html",c)


def tag_view(request,tag_id):
	tag = Tag.objects.get(id=tag_id)
	posts = tag.posts.all()
	c = {"posts":posts,"tag":tag}
	return render(request,"tag/tag_posts.html",c)



class PostDetailView(DetailView):
	model = Post
	template_name = "detail.html"
	context_object_name = "maqola"

	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(*args,**kwargs)
		context["posts"] = Post.objects.all()[:25]
		context["month"] = "yanvar"
		context["category"] = Category.objects.all()
		return context







class CantactPost(View):
	def get(self,request):
		name = request.user
		contact = Contact.objects.get(id=2)
		print(contact)
		form = ContactForm()
		context = {"form":form}
		print(form.errors)
		return render(request,"contact.html",context)

	def post(self,request):
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS,"Xabaringiz qabul qilindi")
			return redirect("blog:contact")
		return render(request,"contact.html")

# from .help 	import paginate_generator
# def my_list(request,list_name):
#     list_objects = None
#     res = {"page":None}
#     if list_name == "tags":
#         list_objects = Tag.objects.all()
#     elif list_name == "categories":
#         list_objects == Category.objects.all()
#     elif list_name == "posts":
#         posts == Post.objects.all()
#         res = paginate_generator(request,posts,5)
#         list_objects = res["list_objects"]
#     c = {"list_objects":list_objects, "page":res["page"] }
#     return render(request,"list.html",c)
        




class PostsView(ListView):
	template_name = "posts.html"
	context_object_name = "posts"

	def get_queryset(self):
		return Post.objects.filter(rating__gte=10)

	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(*args,**kwargs)
		context["posts"] = Post.objects.all()[:25]
		context["category"] = Category.objects.all()
		return context




class UpdatePost(UpdateView):
	model = Post
	form_class = CreatePostForm
	success_url = reverse_lazy("blog:contact")
	template_name = "contact.html"


class CreatePostsView(CreateView):
	model = Comment
	form_class = CommentForm
	success_url = reverse_lazy("blog:bosh")
	template_name = "contact.html"

# class AddPost(UpdateView):
#     model = Post
#     form_class = AddPostForm



class Archiv(MonthArchiveView):
	model = Post
	date_field = "date"
	month_format = "%m"
	template_name = "detail.html"
	context_object_name = "posts"



class ArchivePost(View):
	def get(self,request,year,month,day,day_view):
		if(day_view=="yes"):
			post = Post.objects.filter(date__year=year,date__month=month,date__day=day)
		else:
			post = Post.objects.filter(date__year=year,date__month=month)
		return render(request,"detail.html",{"Post":post})


class DeletePost(DeleteView):
	model = Post
	template_name = "delete.html"	
	success_url = "/"

class DayPost(DayArchiveView):
	model = Post
	date_field = "date"
	month_format = "%m"
	template_name = "day_archive.html"

class DayDetailPost(DateDetailView):
	model = Post
	date_field = "date"
	month_format = "%m"

	def get_contaxt_data(self,*arg,**kwargs):
		context = super().get_context_data(*arg,**kwargs)
		context['categorys'] = Category.objects.all()
		return context 

from .mixin import MyMixinView

class MixinPost(MyMixinView):
	template = "detail.html"
	model_name = Post

def shablonlar(request,template_name):
	template_name='{}.html'.format(template_name)
	return render(request,template_name)
 

	
def json_response(request):
	post = Post.objects.first()
	post_dict = {"title":post.title,
				"category":post.category.title,
				"description":post.description,
				"likes":post.likes,"dislikes":post.dislikes}

	return JsonResponse(post_dict)

class EditPostsView(View):
    def get(self,request,post_id):
        post = Post.objects.get(id=post_id)
        form = CreatePostForm(instance=post)
        return render(request,"contact.html",{"form":form})
    def post(self,request,post_id):
        post = Post.objects.get(id=post_id)
        form = CreatePostForm(request.POST,instance=post)
        # if form.is_valid():
        form.save()
        return redirect("blog:add")
        # else:
            # return render(request,"contact.html",{"form":form})
            


def test(request):
    posts = Post.objects.all()
    print(posts)
    return render(request,"test.html ")

