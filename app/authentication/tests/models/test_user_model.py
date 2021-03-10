from authentication.common.tests.base_test import AuthBaseTestCase, image
from authentication.models import UserManager
from authentication.models import User
from django.contrib.auth import get_user_model


class UserTestCase(AuthBaseTestCase):

    def setUp(self) -> None:
        super(UserTestCase, self).setUp()
        self.user_data = {
            'email': 'test@gmail.com',
            'password': '3gterwqw',
            'avatar': image('avatar.jpeg')
        }
        self.custom_user = User

    def create_test_user(self):
        user = self.custom_user.objects.create(
            email=self.user_data['email'],
            password=self.user_data['password'],
            avatar=self.user_data['avatar']
        )
        user.save()
        return user

    def test_can_create_a_user(self):
        self.custom_user.objects.create(
            email=self.user_data['email'],
            password=self.user_data['password'],
            avatar=self.user_data['avatar']
        )
        normal_user = User.objects.get(email=self.user_data['email'])
        self.assertEqual(normal_user.email, self.user_data['email'])
        self.assertTrue(normal_user.is_active)
        self.assertTrue(normal_user.avatar,
                        '/media/authentication/avatar.jpeg')

    def test_email_field_has_expected_properties(self):
        user = self.create_test_user()
        name = user._meta.get_field('email').name
        self.assertEqual(name, 'email')
        max_length = user._meta.get_field('email').max_length
        self.assertEqual(max_length, 255)
        blank = user._meta.get_field('email').blank
        self.assertFalse(blank)
        null = user._meta.get_field('email').null
        self.assertFalse(null)
        unique = user._meta.get_field('email').unique
        self.assertTrue(unique)

    def test_avatar_field_has_expected_properties(self):
        user = self.create_test_user()
        name = user._meta.get_field('avatar').name
        self.assertEqual(name, 'avatar')
        blank = user._meta.get_field('avatar').blank
        self.assertTrue(blank)
        null = user._meta.get_field('avatar').null
        self.assertTrue(null)
        upload_to = user._meta.get_field('avatar').upload_to
        self.assertEqual(upload_to, 'authentication/avatars/')

    def test_has_date_joined_field(self):
        user = self.create_test_user()
        name = user._meta.get_field('date_joined').name
        self.assertEqual(name, 'date_joined')
        auto_now = user._meta.get_field('date_joined').auto_now
        self.assertTrue(auto_now)

    def test_has_is_active_field(self):
        user = self.create_test_user()
        name = user._meta.get_field('is_active').name
        self.assertEqual(name, 'is_active')
        default = user._meta.get_field('is_active').default
        self.assertTrue(default)

    def test_has_is_staff_field(self):
        user = self.create_test_user()
        name = user._meta.get_field('is_staff').name
        self.assertEqual(name, 'is_staff')
        default = user._meta.get_field('is_staff').default
        self.assertFalse(default)

    def test_other_model_attributes(self):
        self.assertIsInstance(self.custom_user.objects, UserManager)
        self.assertEqual(self.custom_user.USERNAME_FIELD, 'email')
        self.assertEqual(self.custom_user.REQUIRED_FIELDS, [])

    def test_can_create_customer_user(self):
        self.custom_user.objects.create_customer(
            self.user_data['email'],
            self.user_data['password']
        )
        normal_user = User.objects.get(email=self.user_data['email'])
        self.assertEqual(normal_user.email, self.user_data['email'])
        self.assertTrue(normal_user.is_active)
        self.assertFalse(normal_user.is_staff)

    def test_can_create_admin_user(self):
        self.custom_user.objects.create_superuser(
            self.user_data['email'],
            self.user_data['password']
        )
        normal_user = User.objects.get(email=self.user_data['email'])
        self.assertEqual(normal_user.email, self.user_data['email'])
        self.assertTrue(normal_user.is_active)
        self.assertTrue(normal_user.is_staff)
        self.assertTrue(normal_user.is_superuser)

    def test_cannot_create_a_user_without_email(self):
        self.user_data['email'] = ''
        with self.assertRaises(ValueError) as ve:
            self.custom_user.objects._create_user(
                self.user_data['email'],
                self.user_data['password']
            )
        self.assertEqual(str(ve.exception), 'Please provide an email address')

    def test_cannot_create_a_superuser_without_superuser_set_true(self):
        self.user_data['is_superuser'] = False
        with self.assertRaises(ValueError) as ve:
            self.custom_user.objects.create_superuser(
                email=self.user_data['email'],
                password=self.user_data['password'],
                is_superuser=self.user_data['is_superuser']
            )
        self.assertEqual(
            str(ve.exception), 'Superuser must have is_superuser=True.')
