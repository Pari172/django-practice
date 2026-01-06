from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts = {
    "The Future of Remote Work": "As we move further into 2025, hybrid models are evolving into 'fluid workspaces' where location is secondary to synchronous output.",
    "Sustainable Urban Gardening": "Vertical hydroponics and community-led rooftop initiatives are transforming concrete jungles into literal green lungs for the city.",
    "The Rise of Minimalist Tech": "In an era of digital fatigue, a new wave of devices focuses on 'calm technology,' prioritizing utility over constant notifications.",
    "Demystifying Quantum Computing": "While still in its infancy, recent breakthroughs in error correction are bringing us closer to solving climate modeling puzzles.",
    "The Art of Slow Living": "Reclaiming time from the hustle culture involves intentional pauses, manual hobbies, and the radical act of doing absolutely nothing."
}

def index(request):
    # return HttpResponse("We are on blog_post")
    return render(request,'blog_app/index.html', {
        'posts':posts
    })
def all_posts(request):
    #return HttpResponse("We are on all_post")
    return render(request,'blog_app/all_posts.html',{
        "posts":posts
    })

def view_post(request,post):
    return render(request,'blog_app/view_post.html',{
        "post":post,
        "body":posts[post]
    })