from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from ad.models import Post
from ad_rest_api.serializers import AdSerializer

@csrf_exempt
@api_view(['GET', 'POST'])
def post_list(request, format=None):
    '''
    List all ad posts, or create a new post.
    '''
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = AdSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk, format=None):
    '''
    retrive, update or delete a post
    '''
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AdSerializer(post)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = AdSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
