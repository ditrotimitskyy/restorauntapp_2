from django.urls import path
from .views import FoodListView, FoodDetailView, CategoryListView, CategoryDetailView, CreateOrderView, OrderSuccessfullView

urlpatterns = [
    path("category/", CategoryListView.as_view(), name="category-list"),
    path("category/detail/<int:pk>", CategoryDetailView.as_view(), name="category-detail"),
    path("", FoodListView.as_view(), name="food-list"),
    path("food/", FoodListView.as_view(), name="food-list"),
    path("food/detail/<int:pk>", FoodDetailView.as_view(), name="food-description"),
    path("order/", CreateOrderView.as_view(), name='order'),
    path("order/sucsess", OrderSuccessfullView.as_view(), name='order-sucsess')
]