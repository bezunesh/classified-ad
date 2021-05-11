from rest_framework import serializers
from ad.models import Post

'''
 A serializer for model ad.Post
'''
class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'address', 'description', 'email', 'phone', 'published_date']
    