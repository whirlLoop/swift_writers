from authentication.common.tests.base_test import AuthBaseTestCase


class LoginTestCase(AuthBaseTestCase):

    def setUp(self) -> None:
        super(LoginTestCase, self).setUp()

    def test_successful_login_redirects_to_profile_page(self):
        user = self.create_test_customer()
        user.is_active = True
        user.save()
        form = {
            'username': user.email,
            'password': 'password'
        }
        login_request = self.client.post('/accounts/login/', data=form)
        self.assertRedirects(login_request, '/accounts/profile/', 302)

    def test_template_used(self):
        login_request = self.client.get('/accounts/login/')
        self.assertTemplateUsed(
            login_request, 'registration/login.html')
