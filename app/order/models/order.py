from django.db import models
from django.utils import timezone
from order.DAOs.essay_dao import EssayDAO
from order.DAOs.academic_level_dao import AcademicLevelDAO
from order.DAOs.discipline_dao import DisciplineDAO
from authentication.models import User


class Order(models.Model):

    error_messages = {
        'topic': {
            'required': 'Please tell us the topic for this assignment.'
        },
        'type_of_paper': {
            'required': 'Please tell us the type of paper.'
        },
        'due_date': {
            'required': 'Please tell us when this paper should be complete.'
        },
        'academic_level': {
            'required': 'Please tell us your academic level.'
        },
        'citation': {
            'required': 'Please select the referencing style for your paper.'
        },
        'discipline': {
            'required': 'Please tell us your discipline.'
        }
    }

    essays = EssayDAO().objects
    EssayChoices = [
        (item.essay_name, item)
        for item in essays
    ]

    TIME_CHOICES = [
        ('0', '12 am (midnight)'), ('1', '1 am'), ('2', '2 am'),
        ('3', '3 am'), ('4', '4 am'), ('5', '5 am'), ('6', '6 am'),
        ('7', '7 am'), ('8', '8 am'), ('9', '9 am'), ('10', '10 am'),
        ('11', '11 am'), ('12', '12 pm (midnight)'), ('13', '1 pm'),
        ('14', '2 pm'), ('15', '3 pm'), ('16', '4 pm'), ('17', '5 pm'),
        ('18', '6 pm'), ('19', '7 pm'), ('20', '8 pm'), ('21', '9 pm'),
        ('22', '10 pm'), ('23', '11 pm'),
    ]

    academic_levels = AcademicLevelDAO().objects
    ACADEMICLEVELCHOICES = [
        (item.academic_level_name, item.academic_level_display_name)
        for item in academic_levels
    ]

    disciplines = DisciplineDAO().objects
    DISCIPLINE_CHOICES = [
        (item.discipline_id, item._discipline_name)
        for item in disciplines
    ]

    client = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='orders'
    )
    date_created = models.DateTimeField(default=timezone.now)
    topic = models.CharField(
        max_length=255,
        blank=False,
        error_messages=error_messages['topic'],
        verbose_name='Assignment Topic',
        db_index=True
    )
    type_of_paper = models.CharField(
        default='essay',
        choices=EssayChoices,
        error_messages=error_messages['type_of_paper'],
        max_length=80,
        verbose_name='Type of paper'
    )
    no_of_pages = models.IntegerField(
        verbose_name='Pages',
        default=1
    )
    words = models.IntegerField(
        verbose_name='Words',
        null=True,
        blank=True
    )
    due_date = models.DateField(
        verbose_name='Due Date',
        error_messages=error_messages['due_date']
    )
    due_time = models.CharField(
        max_length=2,
        choices=TIME_CHOICES,
        default='0'
    )
    academic_level = models.CharField(
        error_messages=error_messages['academic_level'],
        default='college',
        max_length=80,
        verbose_name='Academic Level',
        choices=ACADEMICLEVELCHOICES
    )
    citation = models.CharField(
        error_messages=error_messages['citation'],
        default='APA 6',
        max_length=255,
        verbose_name='Format / Citation'
    )
    discipline = models.CharField(
        error_messages=error_messages['discipline'],
        max_length=255,
        verbose_name='Discipline',
        choices=DISCIPLINE_CHOICES,
        default=1
    )
    description = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('date_created',)
