from datetime import date
from django import forms
from order.models import Order, OrderMaterial


class OrderForm(forms.ModelForm):

    materials = forms.FileField(required=False)

    class Meta:
        model = Order
        fields = [
            'topic', 'type_of_paper',
            'no_of_pages', 'words', 'due_date', 'due_time',
            'academic_level', 'citation', 'discipline', 'description'
        ]
        description_placeholder = (
            'Describe what you need our writers to do. Add any other '
            'information you think might be useful'
        )
        widgets = {
            'topic': forms.TextInput(
                attrs={'placeholder': 'Tell us the topic.'}),
            'words': forms.HiddenInput(
                attrs={'placeholder': 'Tell us the number of words.'}),
            'due_date': forms.DateInput(
                attrs={
                    'placeholder': 'Select due date.',
                    'min': date.today(),
                    'type': 'date'}),
            'citation': forms.HiddenInput(),
            'description': forms.Textarea(
                attrs={'placeholder': description_placeholder}
            )
        }

    def save(self, request, commit=True):
        order = super().save(commit=False)
        order.client = request.user
        order.status = 'placed'
        if commit:
            order.save()
            self.save_order_materials(request, order)
        return order

    def save_order_materials(self, request, order):
        if request.FILES:
            for file in request.FILES.getlist('materials'):
                material = OrderMaterial.objects.create(
                    order=order,
                    material=file
                )
                material.save()
