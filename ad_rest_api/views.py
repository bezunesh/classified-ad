from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ad.models import Post
from ad_rest_api.serializers import AdSerializer

@csrf_exempt
def post_list(request):
    '''
    List all ad posts, or create a new post.
    '''
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = AdSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def post_detail(request, pk):
    '''
    retrive, update or delete a post
    '''
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=400)
    
    if request.method == 'GET':
        serializer = AdSerializer(post)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AdSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        post.delete()
        return HttpResponse(status=204)
