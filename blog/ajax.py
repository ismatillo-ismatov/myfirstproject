from .models import *
from django.http import JsonResponse
import json

def control_like(request):
    d = request.GET.get('com')
    data = json.loads(d)
    print(data)
    post_id = data["post_id"]
    command = data["command"]
    post = Post.objects.get(id=post_id)
    if  post_id in request.session:
        pass
    else:
        if command == "like":
            post.likes += 1
        else:
            post.dislikes += 1
    post.save()
    request.session[post_id] = True
        
    data = {'likes':post.likes,'dislikes':post.dislikes}
    return JsonResponse(data)
