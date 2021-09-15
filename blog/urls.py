from user.views import *
from django.urls import path
from .controller import *
from .ajax import *
from .views import *
from .ajax import *
app_name = 'blog'

# PostsView
urlpatterns = [
   
   path('list', PostsView.as_view(),name="list"),
   # path('post/<int:pk>',PostDetailView.as_view(),name="post_detail"),
   path('add', CreatePostsView.as_view(),name="add"),
   path('edit/<int:post_id>', EditPostsView.as_view(),name="edit"),
   path('update/<int:pk>', UpdatePost.as_view(),name="update"),
   path('delete/<int:pk>', DeletePost.as_view(),name="delete"),
   # path("<int:year>/<int:month>/<int:day>",MixinPost.as_view(),name="date_archive"),
   path('shablon/<str:template_name>',shablonlar,name="shablonlar"),
   path('<int:year>/<int:month>/<int:day>/<str:day_view>',ArchivePost.as_view(),name="archive"),
   path('contact',CantactPost.as_view(),name="contact"),
   path("tag/<int:tag_id>",tag_view, name="tag_view"),
   path("tag/<int:tag_id>/posts",tag_view, name="tag_view"),
   path('get/<int:tag_id>',get_url,name="get_url"),
   path('category/<str:category_slug>/posts',CategoryPostsView.as_view(),name="category_view"),
   path('json', json_response,name="json_response"),
   path('', IndexView.as_view(),name="bosh"),
   path('post/<int:post_id>',MixinPost.as_view(), name="post_detail"),
   # path("str:list_name>/list",my_list,name="my_list"),
   path("control_like",control_like,name="control_like"),
   path("test",test,name="test"), 
   path("rest",rest_api,name="rest"),
   # path("control_like",control_like,name="control_like")
]
