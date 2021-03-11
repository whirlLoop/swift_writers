# Generated by Django 3.1.6 on 2021-03-10 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('date_joined', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='authentication/avatars/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]