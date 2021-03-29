from authentication.common.tests.base_test import AuthBaseTestCase


class LoginTestCase(AuthBaseTestCase):

    def setUp(self) -> None:
        super(LoginTestCase, self).setUp()
        self.user = self.create_test_customer()
        self.user.is_active = True
        self.user.save()
        form = {
            'username': self.user.email,
            'password': 'password'
        }
        self.login_request = self.client.post('/accounts/login/', data=form)

    def test_successful_login(self):
        self.assertIn('_auth_user_id', self.client.session)
        self.assertRedirects(self.login_request, '/accounts/profile/', 302)

    def test_template_used(self):
        self.client.post('/accounts/logout/')
        get_login = self.client.get('/accounts/login/')
        self.assertTemplateUsed(
            get_login, 'registration/login.html')

    def test_can_log_out(self):
        self.assertIn('_auth_user_id', self.client.session)
        self.client.post('/accounts/logout/')
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_logout_redirects_home(self):
        logout_request = self.client.post('/accounts/logout/')
        self.assertRedirects(logout_request, '/', 302)
