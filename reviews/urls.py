from django.urls import path
from . import views
urlpatterns = [
    # path("", views.review1),
    path("", views.ReviewView.as_view()),
    path("thank-you",views.thank_you),
]
