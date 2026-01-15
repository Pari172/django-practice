from django.urls import path
from . import views

app_name = "blog_app"
urlpatterns = [
    path('', views.index, name="index"),
    path('all_posts/',views.all_posts, name="all_posts"),
    path('<slug:slug>/',views.view_post, name='view_post'),
]