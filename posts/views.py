from django.shortcuts import get_object_or_404, render
from .models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all().order_by("-created_at")
    context = {
        "posts": posts,
    }
    return render(request, "posts/home.html", context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        "post": post,
    }
    return render(request, "posts/detail.html", context)
