from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from authentication.common.tests.base_test import AuthBaseTestCase
from authentication.forms.change_form import AvatarUpdateForm
from order.forms import OrderForm
from authentication.presentation.views import (
    UserProfileView, AvatarUpdateView)
from common.tests.base_test import image


class ProfileViewTestCase(AuthBaseTestCase):

    def setUp(self) -> None:
        super(ProfileViewTestCase, self).setUp()
        self.user = self.create_test_customer()
        self.user.is_active = True
        self.user.save()
        self.client.login(username=self.user, password='password')

    def test_user_profile_view_properties(self):
        self.assertTrue(issubclass(UserProfileView, LoginRequiredMixin))
        self.assertTrue(issubclass(UserProfileView, TemplateView))
        self.assertEqual(UserProfileView.permission_denied_message,
                         'You need to be logged in to view your profile.')
        self.assertEqual(UserProfileView.template_name,
                         'registration/profile.html')

    def test_get_profile_page_request_200_OK(self):
        profile_request = self.client.get('/accounts/profile/')
        self.assertEqual(profile_request.status_code, 200)
        self.assertTemplateUsed(
            profile_request, 'registration/profile.html')
        self.assertEqual(
            profile_request.context['avatar_update_form'], AvatarUpdateForm)
        self.assertEqual(
            profile_request.context['order_form'], OrderForm)

    def test_can_update_avatar(self):
        form = {
            'avatar': image('test_avatar.jpeg')
        }
        avatar_change_request = self.client.post(
            '/accounts/profile/avatar/', data=form)
        self.assertRedirects(avatar_change_request, '/accounts/profile/', 302)

    def test_avatar_update_view_properties(self):
        form = {
            'avatar': image('test_avatar.jpeg')
        }
        avatar_change_request = self.client.post(
            '/accounts/profile/avatar/', data=form, follow=True)
        self.assertEqual(avatar_change_request.context['user'], self.user)
        self.assertTrue(isinstance(
            AvatarUpdateView.form_class(), AvatarUpdateForm))

    def test_avatar_edit_success_returns_message(self):
        form = {
            'avatar': image('test_avatar.jpeg')
        }
        avatar_change_request = self.client.post(
            '/accounts/profile/avatar/', data=form, follow=True)
        message = list(
            avatar_change_request.context.get('messages'))[0]
        self.assertEqual(message.tags, 'success')
        s_msg = ('Your avatar has been changed successfully')
        self.assertTrue('{}'.format(s_msg) in message.message)
