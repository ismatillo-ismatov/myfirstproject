from blog.models import *
from rest_framework import serializers


class CategorySerializator(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("title", "slug","posts_count")