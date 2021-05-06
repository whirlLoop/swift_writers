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
from django.contrib.auth import get_user_model
from authentication.token import account_activation_token
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from order.DAOs.essay_dao import EssayDAO
from order.DAOs.academic_level_dao import AcademicLevelDAO
from order.domain_objects.initial_order import InitialOrder
from order.initial_order_data_context_manager import (
    InitialOrderDataContextManager)


class OrderInitializationForm(forms.Form):
    """Enables a client to initiate the ordering process
    """

    error_messages = {
        'email': {
            'required': 'Please provide your email.'
        },
        'academic_level': {
            'required': 'Please select your academic level.'
        },
        'type_of_paper': {
            'required': 'Please select the type of essay.'
        },
        'no_of_pages': {
            'required': 'Please provide the no of pages.',
            'min_value': 'Ensure number of pages is greater than or equal to 1.'
        },
        'due_date': {
            'required': 'Please provide the due date.',
            'invalid': 'Please provide a valid date format, '
                        'should be yyyy-mm-dd.'
        },
        'total_cost': {
            'required': 'Order cost is required.'
        }
    }

    def __init__(self, *args, **kwargs):
        """Initializes the form data.

        Args:
            essays (list): a list of essays for client to select
            academic_levels (list): a list of academic levels for client to
                select
        """
        essays = EssayDAO().objects
        academic_levels = AcademicLevelDAO().objects
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
        self.fields['type_of_paper'].choices = EssayChoices

    email = forms.EmailField(
        error_messages=error_messages['email'],
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    academic_level = forms.ChoiceField(
        error_messages=error_messages['academic_level'],
        required=True,
    )
    type_of_paper = forms.ChoiceField(
        error_messages=error_messages['type_of_paper'],
        required=True,
    )
    no_of_pages = forms.IntegerField(
        error_messages=error_messages['no_of_pages'],
        initial=1,
        min_value=1,
        widget=forms.widgets.NumberInput(attrs={'min': 1})
    )
    due_date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={
                'min': date.today(),
                'placeholder': 'Select due date', 'type': 'date',
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
        user = self.register_customer(context['password'])
        context['token'] = account_activation_token.make_token(user)
        context['uid'] = urlsafe_base64_encode(force_bytes(user.pk))
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
            'activation_link': current_site.domain + '/activate',
            'support_link': current_site.domain + '/support',
            'profile_link': current_site.domain + '/profile',
            'root_url': current_site.domain + '/',
            'protocol': 'https' if request.is_secure() else 'http',
            'domain': current_site.domain
        }
        return context

    def generate_password(self):
        password_characters = string.ascii_letters + \
            string.digits
        password = ''.join(random.choice(password_characters)
                           for i in range(12))
        return password

    def register_customer(self, password):
        user_model = get_user_model()
        user = user_model.objects.create_customer(
            self.cleaned_data['email'], password)
        return user

    def set_form_data_to_context(self, request):
        context_object = InitialOrderDataContextManager(request)
        form_data = self.cleaned_data
        context_object.set_initial_order_data_to_context(form_data)
