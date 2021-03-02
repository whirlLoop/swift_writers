"""Order Initialization form.
"""
import random
import string
from datetime import date
from django.contrib.sites.shortcuts import get_current_site
from django import forms
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


class OrderInitializationForm(forms.Form):
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
        'due_date': {
            'required': 'Please provide the due date'
        }
    }

    def __init__(self, essays, academic_levels, *args, **kwargs):
        """Initializes the form data.

        Args:
            essays (list): a list of essays for client to select
            academic_levels (list): a list of academic levels for client to
                select
        """
        super(OrderInitializationForm, self).__init__(*args, **kwargs)

        AcademicLevelChoices = [
            (item.academic_level_name, item.academic_level_display_name)
            for item in academic_levels
        ]
        self.fields['academic_level'].choices = AcademicLevelChoices
        EssayChoices = [
            (item.essay_name, item.essay_display_name)
            for item in essays
        ]
        self.fields['essay'].choices = EssayChoices

    email = forms.EmailField(
        error_messages=error_messages['email'],
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    academic_level = forms.ChoiceField(
        error_messages=error_messages['academic_level'],
        required=True,
    )
    essay = forms.ChoiceField(
        error_messages=error_messages['essay'],
        required=True,
    )
    total_cost = forms.DecimalField(
        widget=forms.HiddenInput
    )
    no_of_pages = forms.IntegerField(
        initial=1,
        widget=forms.widgets.NumberInput(attrs={'min': 1})
    )
    due_date = forms.DateField(
        widget=forms.DateInput(
            format=('%d/%m/%Y'),
            attrs={
                'min': date.today(),
                'placeholder': 'Select a date', 'type': 'date',
                'class': 'datepicker-input'}),
        error_messages=error_messages['due_date'],
    )

    def send_email(self, request):
        to_email = self.cleaned_data['email']
        from_email = settings.VERIFIED_EMAIL_USER
        context = self.setup_context_data(request, to_email)
        subject = (
            "Registration completed. Check your login details and "
            "finish up your order for free!"
        )
        html_content = render_to_string(
            "email/initialize_registration_email.html", context
        )
        if subject and from_email:
            email_message = EmailMultiAlternatives(
                subject, None, from_email, [to_email]
            )
            email_message.attach_alternative(html_content, 'text/html')
            email_message.send()

    def setup_context_data(self, request, email):
        current_site = get_current_site(request)
        generated_password = self.generate_password()
        context = {
            'email': email,
            'password': generated_password,
            'login_link': current_site.domain + '/login',
            'support_link': current_site.domain + '/support',
            'profile_link': current_site.domain + '/profile',
            'protocol': 'https' if request.is_secure() else 'http',
        }
        return context

    def generate_password(self):
        password_characters = string.ascii_letters + \
            string.digits
        password = ''.join(random.choice(password_characters)
                           for i in range(12))
        return password
