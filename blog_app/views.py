from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404,redirect
from .models import Post
from django import views
from django.views.generic import ListView,DetailView
from django.views import View
from .forms import CommentForm
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


# as we need to handle post request comming from comment form DetailView will not work we are commenting it out
# class PostDetailView(DetailView):
#     template_name = "blog_app/view_post.html"
#     model = Post
#     context_object_name = "post"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["tags"] = self.object.tags.all()
#         context["comment_form"] = CommentForm()
#         return context
    
class PostDetailView(View):
    def get(self,request,slug):
        post = Post.objects.get(slug=slug)
        stored_posts = request.session.get("stored_posts",[])
        is_read_later=post.id in stored_posts
        context = {
            "post":post,
            "tags":post.tags.all(),
            "comment_form":CommentForm(),
            "comments":post.comments.all().order_by("-id"),
            "is_read_later":is_read_later
        }
        return render(
            request,
            "blog_app/view_post.html",
            context
        )

    # we are already getting slug while passing through form in action tag
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("blog_app:view_post", args=[slug]))
        stored_posts = request.session.get("stored_posts",[])
        is_read_later = post.id in stored_posts
        context = {
            "post":post,
            "tags":post.tags.all(),
            "comment_form":comment_form,
            "comments":post.comments.all().order_by("-id"),
            "is_read_later":is_read_later
        }

        return render(request,"blog_app/view_post.html",context)

class ReadLaterView(View):
    def get(self,request):
        stored_posts = request.session.get("stored_posts")
        context = {}
        if stored_posts is None or len(stored_posts)==0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
        return render(request,"blog_app/read_later_posts.html",context)

    def post(self,request):
        stored_posts = request.session.get("stored_posts",[])
        # if stored_posts is None:    we can just add [] in above line
        #     stored_posts=[]
        post_id = int(request.POST["post_id"])
        if "remove" in request.POST:
            if post_id in stored_posts:
                stored_posts.remove(post_id)
        else: 
            if post_id not in stored_posts:
                stored_posts.append(int(request.POST["post_id"]))
            
        request.session["stored_posts"] = stored_posts
        post = Post.objects.get(id=post_id)
        return redirect("blog_app:view_post",slug=post.slug)