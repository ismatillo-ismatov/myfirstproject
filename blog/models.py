from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings
from django.utils.timezone import timezone
from django.urls import reverse

def image_folder(post,filename):
	category_name = post.category.title
	post_name = post.title
	file_format = filename.split('.')[-1]
	file_name = "{}.{}".format(post_name,file_format)
	post_image_folder = "{}/{}/{}".format(category_name,post_name,file_name)
	return post_image_folder


def check_slug(slug):
    for s in slug:
        if s.isdigit():
            raise ValidationError("%(slug)s ichida raqam topildi. Raqam ishlatmang",code="invalid",params={"slug":slug})

class Category(models.Model): # blog_category
	title = models.CharField(max_length=75,	blank=True,verbose_name= 'Katalog nomi')
	slug = models.SlugField(max_length=75,unique=True,help_text="Kalit so'z")
	image = models.ImageField(upload_to="images")
	posts_count = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-id"]
		verbose_name = 'Kategoriya'
		verbose_name_plural = 'Kategoriyalar'


	def get_absolute_url(self):
		return reverse("blog:category_view", kwargs={"category_slug": self.slug})

class Tag(models.Model):
	
	title = models.CharField("Teg nomi", max_length=50)
	
	def __str__(self):
		return self.title


	def get_url(self):
		return reverse("blog:tag_view", kwargs= {"tag_id": self.id})





class Post(models.Model):
	category = models.ForeignKey(Category,related_name="postlar",on_delete=models.CASCADE,verbose_name='Kategoriya') # id
	title = models.CharField(max_length=75,	blank=True,verbose_name='Maqola nomi')
	tags = models.ManyToManyField(Tag,verbose_name="Foydali teglar",related_name="posts")
	description = models.TextField()
	image = models.ImageField(upload_to=image_folder)
	likes = models.PositiveIntegerField(default=0)
	dislikes = models.PositiveIntegerField(default=0)
	heart = models.PositiveIntegerField(default=0)
	rating = models.PositiveIntegerField(default=0)
	views = models.PositiveIntegerField(default=0)
	date = models.DateField(auto_now_add=True)
	 
	 
	class Meta:
		ordering = ['-id']

	def __str__(self):
		return self.title

class UserData(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,related_name='userdata',verbose_name='User data') # id
	adress = models.CharField("Manzil",blank=True, max_length=50)
	phone = models.CharField("Telefon", max_length=50)
	card_number = models.PositiveIntegerField(default=0)
	like_dislike = models.ManyToManyField(Post)

class Comment(models.Model):
	category = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="commentlar", verbose_name="commentlar",null=True)
	user = models.ForeignKey(UserData,on_delete=models.CASCADE,related_name="author",verbose_name="category",null=True)
	email = models.EmailField(max_length=100)
	description = models.TextField(blank=True,verbose_name="fikrlar")
	likes = models.PositiveIntegerField(default=0)
	check = models.BooleanField(default=False)


	



	class Meta:
		
		verbose_name = "User ma'lumot"
		verbose_name_plural = "User ma'lumotlari"
  
class Contact(models.Model):
    name = models.CharField(max_length=17)
    surname = models.CharField(max_length=20)
    msg = models.TextField()
    phone = models.CharField(max_length=25)



    def __str__(self):
     
    	return self.name


# class PostHelp(models.Model):
# 	img = models.ImageField()
# 	desc = models.TextField()




# all create get save delete	

	# FIELDNAME = models.EmailField()
	# FIELDNAME = models.TextField()
	
	# FIELDNAME = models.BooleanField(default=False)
	
	# FIELDNAME = models.NullBooleanField()

	# FIELDNAME = models.IntegerField()
	# FIELDNAME = models.SmallIntegerField()
	# FIELDNAME = models.BigIntegerField()
	# FIELDNAME = models.PositiveIntegerField()
	# FIELDNAME = models.PositiveSmallIntegerField()
	# FIELDNAME = models.FloatField()
	# FIELDNAME = models.DecimalField(, max_digits=5, decimal_places=2)
	# FIELDNAME = models.DateTimeField(auto_now_add=True)
	# FIELDNAME = models.DateField(auto_now=True)
	# FIELDNAME = models.TimeField()
	# FIELDNAME = models.DurationField()
	# FIELDNAME = models.BinaryField()
	# FIELDNAME = models.AutoField()
	# FIELDNAME = models.BigAutoField()
	# FIELDNAME = models.EmailField()
	# FIELDNAME = models.URLField("HTTP://GOOGLE.COM")
	# FIELDNAME = models.ImageField(upload_to='images')
	# FIELDNAME = models.FileField(upload_to='files')