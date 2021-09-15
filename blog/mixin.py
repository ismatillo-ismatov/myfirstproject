from .models import *
from .forms import *
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

class MyMixinView(View):
    template = None
    model_name = None

    def get(self,request,post_id):
        post = self.model_name.objects.get(id=post_id)
        data = {"maqola":post}
        # comment = Comment.objects.get(id=post_id)
        form = ComForm()
        post.views += 1
        post.save()
        comment = post.commentlar.filter(check=True)[:5]
        data["posts"] = Post.objects.all()[:25]         
        data["category"] = Category.objects.all()
        data["tags"] = Tag.objects.all()
        data["comment"] = comment
        data["form"] = form
        return render (request,self.template,data)

    def post(self,request,post_id):
        post = Post.objects.get(id=post_id)
        u = request.user
        user = UserData.objects.get(user=u)
        form = ComForm(request.POST)
        print(form)
        print(form)
        if form.is_valid():
          f = form.save(commit=False)
          f.post = post
          f.user = user
          f.save()
          messages.add_message(request,messages.SUCCESS,"kamentingiz tekshirilgangan song chiqadi")
        else:
            messages.add_message(request,messages.DANGER,"kamentingiz qabul qilinmadi")
        # Comment.objects.create(category=post,user=user,email=email,description=comment)
        return HttpResponseRedirect(reverse('blog:post_detail', kwargs={'post_id':post_id}))