# Generated by Django 3.1.6 on 2021-04-27 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20210426_1930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordermaterial',
            options={'ordering': ('order',)},
        ),
        migrations.RemoveField(
            model_name='ordermaterial',
            name='extension',
        ),
    ]
