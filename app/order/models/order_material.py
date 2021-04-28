import os
import pathlib
from django.db import models
from order.models import Order


def user_directory_path(instance, filename):
    return (
        'orders/{0}/materials/{1}/{2}'.format(
            instance.order.client, instance.order, filename)
    )


class OrderMaterial(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='materials'
    )
    material = models.FileField(
        upload_to=user_directory_path
    )

    @property
    def extension(self):
        return pathlib.Path(self.material.name).suffix

    @property
    def filename(self):
        return os.path.basename(self.material.name)

    def __str__(self) -> str:
        return self.filename

    class Meta:
        ordering = ('order',)
