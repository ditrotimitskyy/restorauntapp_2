from django.forms import ModelForm, ModelChoiceField

from .models import Order, Food
class CreateOrderForm(ModelForm):
    food = ModelChoiceField(queryset=Food.objects, empty_label="виберіть страву")
    class Meta :
        model = Order
        fields = [
            "amount",
            "adress",
        ]