from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy


from .models import Food, Category, Order
from .forms import CreateOrderForm

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

class CreateOrderView(CreateView):
    model = Order 
    template_name = "restorauntapp/order.html"
    form_class = CreateOrderForm
    success_url = reverse_lazy("order-sucsess")
    

    def form_valid(self, form):
        user = User.objects.get(username = self.request.user.username)
        form.instance.user = user
        return super().form_valid(form)
    
class OrderSuccessfullView(TemplateView):
    template_name = "restorauntapp/ordersucsess.html"