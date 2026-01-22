from django.urls import path
from . import views
urlpatterns = [
    # path("", views.review1),
    path("", views.ReviewView.as_view()),
    # path("thank-you",views.thank_you),
    # path("thank-you",views.ThankYou.as_view()),
    # path("thank-you",views.ThankYouView.as_view()),
    # path("thank-you",views.ReviewsListView.as_view()),
    path("thank-you",views.ReviewListView.as_view()),
    path("favorite",views.AddFevoriteView.as_view()),
    path("<int:id>",views.SingleReviewView.as_view()),
]