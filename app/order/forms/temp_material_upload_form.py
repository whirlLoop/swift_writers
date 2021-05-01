from django import forms
from order.models import TempOrderMaterial


class TempMaterialUploadForm(forms.ModelForm):

    class Meta:
        model = TempOrderMaterial
        fields = ['client', 'material']

    def save(self, request, commit=True):
        material = super().save(commit=False)
        material.client = request.user
        if commit:
            material.save()
        return material
