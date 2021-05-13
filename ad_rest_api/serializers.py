from rest_framework import serializers
from ad.models import Post, Category
from django.contrib.auth.models import User

'''
 A serializer for model ad.Post
'''
class AdSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'address', 'description', 'email', 'phone', 'published_date', 'author']

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'username', 'posts']

class CategorySerializer(serializers.ModelSerializer):
    #posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = Category
        fields = ['id', 'name']