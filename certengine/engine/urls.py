from django.urls import path
from engine import views
urlpatterns = [
    path("list/", views.CarList.as_view(), name="car_list"),
    path("home/", views.home_view, name="home"),
]