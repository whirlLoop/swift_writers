from datetime import date
from django import forms
from order.models import Order


class OrderForm(forms.ModelForm):

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
                attrs={'placeholder': 'Tell us the number of words instead.'}),
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
