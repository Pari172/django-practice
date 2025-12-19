from django.urls import path
from . import views

app_name = "year_challenge"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:month>/',views.monthly_challenge_by_number),
    path('<str:month>/',views.monthly_challenge,name='monthly_challenge'),
]