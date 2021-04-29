import os
from django.db import models
from django.utils import timezone
from authentication.models import User


def temp_material_directory_path(instance, filename):
    return ('orders/temp_materials/{0}/{1}'.format(instance.client, filename))


class TempOrderMaterial(models.Model):

    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='temp_materials'
    )

    material = models.FileField(
        upload_to=temp_material_directory_path
    )

    date_uploaded = models.DateTimeField(default=timezone.now)

    @property
    def filename(self):
        return os.path.basename(self.material.name)

    def __str__(self) -> str:
        return self.filename

    class Meta:
        ordering = ('date_uploaded',)
