from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from blog.models import Post
# Create your views here.


def index(request):
    sorted_posts = Post.objects.all().order_by('title')
    print(sorted_posts)
    return render(request, "blog/index.html",{
      "posts":sorted_posts
    })


def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/all-posts.html',{
      "all_posts": all_posts
    })

def single_post(request, slug):
    id_post = Post.objects.get(slug=slug)

    return render(request,'blog/post-detail.html',{
      "title":id_post.title,
      "content":id_post.content,
      "image":id_post.image,
      "author":id_post.author,
      "date":id_post.date,

    })
