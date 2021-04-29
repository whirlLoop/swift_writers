# Generated by Django 3.1.6 on 2021-04-29 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import order.models.temp_order_material


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0006_auto_20210427_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempOrderMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.FileField(upload_to=order.models.temp_order_material.temp_material_directory_path)),
                ('date_uploaded', models.DateTimeField(default=django.utils.timezone.now)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temp_materials', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
