from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Food, Category

class FoodDetailView(DetailView):
    model = Food

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class FoodListView(ListView):
    model = Food
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class CategoryListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        food_list = Food.objects.filter(category__id = self.get_object().id)
        context["food_list"] = food_list
        return context
