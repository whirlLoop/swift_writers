# Generated by Django 3.1.6 on 2021-04-23 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('topic', models.CharField(db_index=True, error_messages={'required': 'Please tell us the topic for this assignment.'}, max_length=255, verbose_name='Assignment Topic')),
                ('type_of_paper', models.CharField(choices=[('essay', 'Essay'), ('annotated_bibliography', 'Annotated bibliography'), ('argumentative_essay', 'Argumentative essay'), ('biography', 'Biography'), ('capstone_project', 'Capstone project')], default='essay', error_messages={'required': 'Please tell us the type of paper.'}, max_length=80, verbose_name='Type of paper')),
                ('no_of_pages', models.IntegerField(default=1, verbose_name='Pages')),
                ('words', models.IntegerField(blank=True, null=True, verbose_name='Words')),
                ('due_date', models.DateField(error_messages={'required': 'Please tell us when this paper should be complete.'}, verbose_name='Due Date')),
                ('due_time', models.CharField(choices=[('0', '12 am (midnight)'), ('1', '1 am'), ('2', '2 am'), ('3', '3 am'), ('4', '4 am'), ('5', '5 am'), ('6', '6 am'), ('7', '7 am'), ('8', '8 am'), ('9', '9 am'), ('10', '10 am'), ('11', '11 am'), ('12', '12 pm (midnight)'), ('13', '1 pm'), ('14', '2 pm'), ('15', '3 pm'), ('16', '4 pm'), ('17', '5 pm'), ('18', '6 pm'), ('19', '7 pm'), ('20', '8 pm'), ('21', '9 pm'), ('22', '10 pm'), ('23', '11 pm')], default='0', max_length=2)),
                ('academic_level', models.CharField(choices=[('AL1', 'High School'), ('AL2', 'College'), ('AL3', "Bachelor's"), ('AL4', 'Masters'), ('AL5', 'PhD'), ('AL6', 'Not Applicable')], default='college', error_messages={'required': 'Please tell us your academic level.'}, max_length=80, verbose_name='Academic Level')),
                ('citation', models.CharField(default='APA 6', error_messages={'required': 'Please select the referencing style for your paper.'}, max_length=255, verbose_name='Format / Citation')),
                ('discipline', models.CharField(choices=[('1', 'Business'), ('2', 'English'), ('3', 'Art'), ('4', 'Art History'), ('5', 'Accounting'), ('6', 'Cyber Security'), ('7', 'Computer Science'), ('8', 'Technical Writing'), ('9', 'Computer Science'), ('10', 'Money and Banking'), ('10', 'Sociology')], default=1, error_messages={'required': 'Please tell us your discipline.'}, max_length=255, verbose_name='Discipline')),
                ('description', models.TextField(blank=True, null=True)),
                ('state', models.CharField(choices=[('placed', 'PLACED'), ('confirmed', 'CONFIRMED'), ('healthy', 'HEALTHY'), ('unhealthy', 'UNHEALTHY'), ('dangerous', 'DANGEROUS'), ('critical', 'CRITICAL'), ('indeterminate', 'INDETERMINATE'), ('cancelled', 'CANCELLED'), ('delivered', 'DELIVERED'), ('finished', 'FINISHED')], error_messages={'required': 'Please provide the state for this order.'}, max_length=40)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date_created',),
            },
        ),
    ]
