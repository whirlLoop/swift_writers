# from django.contrib.auth import authenticate
from authentication.common.tests.base_test import AuthBaseTestCase
from authentication.forms.change_form import AvatarUpdateForm
from common.tests.base_test import image


class ProfileViewTestCase(AuthBaseTestCase):

    def setUp(self) -> None:
        super(ProfileViewTestCase, self).setUp()
        self.user = self.create_test_customer()
        self.user.is_active = True
        self.user.save()
        self.client.login(username=self.user, password='password')

    def test_get_profile_page_request_200_OK(self):
        profile_request = self.client.get('/accounts/profile/')
        self.assertEqual(profile_request.status_code, 200)
        self.assertTemplateUsed(
            profile_request, 'registration/profile.html')
        self.assertEqual(
            profile_request.context['avatar_update_form'], AvatarUpdateForm)

    def test_can_update_avatar(self):
        form = {
            'avatar': image('test_avatar.jpeg')
        }
        profile_request = self.client.post(
            '/accounts/profile/avatar/', data=form)
        self.assertRedirects(profile_request, '/accounts/profile/', 302)
