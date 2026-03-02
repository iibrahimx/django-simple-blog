from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Post
from .forms import CommentForm


# Create your views here.
def home(request):
    posts = Post.objects.all().order_by("-created_at")
    context = {
        "posts": posts,
    }
    return render(request, "posts/home.html", context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by("-created_at")

    form = CommentForm()

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post_detail", pk=post.pk)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "posts/detail.html", context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "posts/form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "posts/form.html"

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "posts/confirm_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
