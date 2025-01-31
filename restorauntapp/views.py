from django.views.generic.list import ListView

from .models import Food

class FoodListView(ListView):
    model = Food
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    