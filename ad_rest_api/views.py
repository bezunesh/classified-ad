from rest_framework import generics
from ad.models import Post
from ad_rest_api.serializers import AdSerializer


class PostList(generics.ListCreateAPIView):
    '''
    List all ad posts, or create a new post.
    '''
    queryset = Post.objects.all()
    serializer_class = AdSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    retrive, update or delete a post
    '''
    queryset = Post.objects.all()
    serializer_class = AdSerializer