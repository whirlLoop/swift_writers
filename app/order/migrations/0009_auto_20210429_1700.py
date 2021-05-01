# Generated by Django 3.1.6 on 2021-04-29 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0008_auto_20210429_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempordermaterial',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='temp_materials', to=settings.AUTH_USER_MODEL),
        ),
    ]
