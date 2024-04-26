from rest_framework import serializers
from .models import BlogPost, Category

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        # fields = ['id', 'title', 'content', 'category', 'author', 'created_at']
        fields='__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'