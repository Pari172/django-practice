from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Post
from django import views
from .forms import PostForm
from django.views.generic import ListView,DetailView
# Create your views here.
# posts = {
#     "The Future of Remote Work": "As we move further into 2025, hybrid models are evolving into 'fluid workspaces' where location is secondary to synchronous output.",
#     "Sustainable Urban Gardening": "Vertical hydroponics and community-led rooftop initiatives are transforming concrete jungles into literal green lungs for the city.",
#     "The Rise of Minimalist Tech": "In an era of digital fatigue, a new wave of devices focuses on 'calm technology,' prioritizing utility over constant notifications.",
#     "Demystifying Quantum Computing": "While still in its infancy, recent breakthroughs in error correction are bringing us closer to solving climate modeling puzzles.",
#     "The Art of Slow Living": "Reclaiming time from the hustle culture involves intentional pauses, manual hobbies, and the radical act of doing absolutely nothing."
# }

# def index(request):
#     # return HttpResponse("We are on blog_post")
#     latest_post = Post.objects.all().order_by('date')
#     print(latest_post)
#     return render(request,'blog_app/index.html', {
#         'posts':latest_post
#     })

class IndexView(ListView):
    template_name = "blog_app/index.html"
    model = Post
    ordering = "-date"
    context_object_name="posts"
    #override this method to pass you own data
    def get_queryset(self):
        qs = super().get_queryset()
        return qs

# def all_posts(request):
#     #return HttpResponse("We are on all_post")
#     latest_post = Post.objects.all().order_by('date')
#     return render(request,'blog_app/all_posts.html',{
#         "posts":latest_post
#     })

class AllPostsView(ListView):
    template_name = "blog_app/all_posts.html"
    model = Post
    ordering = "-date"
    context_object_name = "posts"


# def view_post(request,slug):
#     # post = Post.objects.filter(slug=slug) # this will return query set not single oject
#     post = get_object_or_404(Post, slug=slug)
#     tags = post.tags.all()
#     return render(request,'blog_app/view_post.html',{
#         "post":post,
#         "tags":tags
#         # "body":posts[post]
#     })

class PostDetailView(DetailView):
    template_name = "blog_app/view_post.html"
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = self.object.tags.all()
        return context
    