from django.urls import path
from .views import FoodListView

urlpatterns = [
    path("food/", FoodListView.as_view(), name="food-list"),
]