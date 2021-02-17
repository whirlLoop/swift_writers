"""Order creation form.
"""
from django import forms
from order.DAOs.essay_dao import EssayDAO
from order.DAOs.academic_level_dao import AcademicLevelDAO


class OrderCreationForm(forms.Form):
    """Enables a client to initiate the ordering process
    """

    error_messages = {
        'email': {
            'required': 'Please provide your email'
        },
        'academic_level': {
            'required': 'Please select your academic level'
        },
        'essay': {
            'required': 'Please select the type of essay'
        },
        'duration': {
            'required': 'Please provide the duration'
        }
    }

    AcademicLevelChoices = [
        (i, AcademicLevelDAO().get_academic_levels()[i].
         academic_level_name) for i in range(
            1, (len(AcademicLevelDAO().get_academic_levels())))
    ]

    EssayChoices = [
        (i, EssayDAO().get_essays()[i].essay_name) for i in range(
            1, (len(EssayDAO().get_essays())))
    ]

    DurationChoices = [
        ('D1', '6 hrs'),
        ('D2', '8 hrs'),
        ('D3', '12 hrs'),
        ('D4', '18 hrs'),
        ('D5', '1 day'),
        ('D6', '2 days'),
        ('D7', '3 days'),
        ('D8', '4 days'),
        ('D9', '5 days'),
        ('D10', '6 days'),
        ('D11', '1 Week'),
        ('D12', '2 Weeks'),
        ('D13', '3 Weeks'),
        ('D14', '1 Month'),
        ('D15', 'custom'),
    ]

    email = forms.EmailField(
        error_messages=error_messages['email'],
        required=True
    )
    academic_level = forms.ChoiceField(
        error_messages=error_messages['academic_level'],
        required=True,
        choices=AcademicLevelChoices
    )
    essay = forms.ChoiceField(
        error_messages=error_messages['essay'],
        required=True,
        choices=EssayChoices
    )
    duration = forms.ChoiceField(
        error_messages=error_messages['duration'],
        required=True,
        choices=DurationChoices
    )
    total_cost = forms.DecimalField(
        widget=forms.HiddenInput
    )
    no_of_pages = forms.IntegerField(
        initial=1
    )
