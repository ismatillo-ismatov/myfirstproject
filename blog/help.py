# from django.core.paginator import Paginator
# from .models import *


# def paginate_generator(request,objects_list,limit):
#     paginator = Paginator(objects_list,limit)
#     if "page" in request.GET:
#         page_num = request.GET['page']
#     else:
#         page_num = 1
#     page = paginator.get_page(page_num)
    
#     result = {"list_objects":page.object_list,"page":page}
#     return result
                     