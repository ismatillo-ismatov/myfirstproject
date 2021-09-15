from .models import Post

def most_view(request):
    p = Post.objects.all()
    context = {}
    context["most_view"] = p.order_by("-views")[:5]
    return context