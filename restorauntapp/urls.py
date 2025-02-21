from django.urls import path
from .views import FoodListView, FoodDetailView, CategoryListView, CategoryDetailView

urlpatterns = [
    path("category/", CategoryListView.as_view(), name="category-list"),
    path("category/detail/<int:pk>", CategoryDetailView.as_view(), name="category-detail"),
    path("", FoodListView.as_view(), name="food-list"),
    path("food/", FoodListView.as_view(), name="food-list"),
    path("food/detail/<int:pk>", FoodDetailView.as_view(), name="food-description")
]