from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
#from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from ad.models import Post
from ad_rest_api.serializers import AdSerializer


class PostList(APIView):
    '''
    List all ad posts, or create a new post.
    '''
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = AdSerializer(posts, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    '''
    retrive, update or delete a post
    '''
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = AdSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = AdSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
