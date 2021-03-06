from datetime import date
from django import forms
from order.models import Order, TempOrderMaterial, OrderMaterial
from django_mysql.forms import SimpleListField
from order.context_processors import initial_order


class OrderForm(forms.ModelForm):

    materials = SimpleListField(
        forms.IntegerField(), required=False, widget=forms.HiddenInput())

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
            self.save_materials(order)
        return order

    def save_materials(self, order):
        materials = self.cleaned_data['materials']
        for pk in materials:
            temp_material = TempOrderMaterial.objects.get(id=pk)
            material = OrderMaterial.objects.create(
                order=order,
                material=str(temp_material)
            )
            material.save()
            temp_material.delete()

    def set_initial_data(self, data):
        for key, value in data.items():
            if key in self.fields:
                self.fields[key].initial = value
