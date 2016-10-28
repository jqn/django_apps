from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post
from blog.forms import PostForm


def home(request):
    tmpl_vars = {form: 'PostForm'}
    return reder(request, 'home.html', tmpl_vars)


@api_view(['GET'])
def post_collection(request):
    if request.method == 'GET':
        posts = post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def post_element(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
