from django.contrib import admin
from  .models import * 
# Register your models here.


# admin.site.register(Comment)
class CommentAdmin(admin.TabularInline):
    model = Comment
    row_id_field = ['post']

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
	list_display = ["id","title","top","category", "image", "likes"]
	list_display_links = ["title"]
	# list_editable = ["likes"]
	search_fields = ("title",)
	list_filter = ["category"]
	readonly_fields = ['likes','dislikes','heart','rating','views']
	inlines = [CommentAdmin]

	def top(self,instanse):
		if instanse.views > 50:
			return "Top"
		else:
			return "----"
admin.site.register(Category)
class AdminCategory(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    

    

admin.site.register(UserData)
admin.site.register(Tag)
admin.site.register(Contact)
