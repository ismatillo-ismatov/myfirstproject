from re import T

from django.http.response import JsonResponse
from api.serializers import CategorySerializator
from django.shortcuts import render
from rest_framework import serializers
from django.http import JsonResponse 
from blog.models import *
from .serializers import CategorySerializator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 


@api_view(['GET', 'POST'])
def categorys_api(request):
    if request.method == "POST":
        serializer = CategorySerializator(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    categorys = Category.objects.all()
    # category = Category.objects.get(pk=pk)
    serializer = CategorySerializator(categorys,many=True)
    
    
    
    return JsonResponse(serializer.data,safe=False)
