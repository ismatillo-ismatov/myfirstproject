from django.shortcuts import render
from django.http import HttpResponse,FileResponse,JsonResponse
from .models import *
from django.db.models import F,Q,Min,Max,Count

# Create your views here.

import random

def index(request,post_id):
	p = Post.objects.get(id=post_id)
	print(p)
	img = open("images/index2.jpeg",'rb')

	#return FileResponse(img)
	return HttpResponse("<h1>Hello</h1>")

def rest_api(request):
    posts = Post.objects.all().order_by ('id')[:8]
    data = {"posts":[]}
    for p in posts:
        d = {
			'id':p.id,
			'title':p.title,
			'category':p.category.title,
			'image':p.image.url,
			'description':p.description,
			'heart':p.heart,
			'rating':p.rating,
			'likes':p.likes,
			'dislikes':p.dislikes,
			'date':p.date
		}
        data['posts'].append(d)
    print(data)
    
    return JsonResponse(data)
		
			
		
















# 	2020 12 28 10-dars