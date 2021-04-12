from django import forms
from order.models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['topic', 'type_of_paper', 'no_of_pages']
