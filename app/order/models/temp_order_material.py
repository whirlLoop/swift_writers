import os
from django.db import models
from django.utils import timezone
from authentication.models import User


def temp_material_directory_path(instance, filename):
    return ('orders/temp_materials/{0}/{1}'.format(instance.client, filename))


class TempOrderMaterial(models.Model):

    error_messages = {
        'material': {
            'required': 'Please provide the material.'
        }
    }

    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='temp_materials',
        null=True,
        blank=True
    )

    material = models.FileField(
        upload_to=temp_material_directory_path,
        error_messages=error_messages['material']
    )

    date_uploaded = models.DateTimeField(default=timezone.now)

    @property
    def filename(self):
        return os.path.basename(self.material.name)

    def __str__(self) -> str:
        return self.material.name

    class Meta:
        ordering = ('date_uploaded',)
