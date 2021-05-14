from rest_framework import serializers
from ad.models import Post, Category
from django.contrib.auth.models import User

'''
 A serializer for model ad.Post
'''
class AdSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    desc = serializers.HyperlinkedIdentityField(view_name='post-description', format='html')

    class Meta:
        model = Post
        fields = ['url', 'id', 'desc', 'title', 'category', 'address', 'description', 'email', 'phone', 'published_date', 'author']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'posts']

class CategorySerializer(serializers.ModelSerializer):
    #posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = Category
        fields = ['id', 'name']