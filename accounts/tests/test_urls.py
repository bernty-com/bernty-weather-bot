from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase

from accounts.urls import (app_name, urlpatterns)
from accounts import views
from accounts.views import (
    account_activation_sent,
    account_activation_fail,
    change_password
    )

# python manage.py test accounts.tests.test_urls --keepdb
class UrlTests(TestCase):
    def test_urls_login_status_code(self):
        name = app_name + ':login'
        url = reverse(name)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_resolve_url_login(self):
        resolver = resolve('/accounts/login/')
        self.assertEqual(resolver.url_name, 'login')
 
    def test_urls_logout_status_code(self):
        name = app_name + ':logout'
        url = reverse(name)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_resolve_url_logout(self):
        resolver = resolve('/accounts/logout/')
        self.assertEqual(resolver.url_name, 'logout')

    def test_urls_signup_status_code(self):
        name = app_name + ':signup'
        url = reverse(name)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_resolve_url_signup(self):
        resolver = resolve('/accounts/signup/')
        self.assertEqual(resolver.url_name, 'signup')

    def test_urls_login_status_profile(self):
        name = app_name + ':profile'
        url = reverse(name)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    def test_resolve_url_profile(self):
        resolver = resolve('/accounts/profile/')
        self.assertEqual(resolver.url_name, 'profile')

    def test_urls_login_status_account_activation_sent(self):
        name = app_name + ':account_activation_sent'
        url = reverse(name)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_resolve_url_account_activation_sent(self):
        resolver = resolve('/accounts/account_activation_sent/')
        self.assertEqual(resolver.url_name, 'account_activation_sent')
        self.assertEquals(resolver.func, account_activation_sent)

    def test_urls_login_status_account_activation_fail(self):
        name = app_name + ':account_activation_fail'
        url = reverse(name)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_resolve_url_account_activation_fail(self):
        resolver = resolve('/accounts/account_activation_fail/')
        self.assertEqual(resolver.url_name, 'account_activation_fail')
        self.assertEquals(resolver.func, account_activation_fail)

    def test_urls_login_status_change_password(self):
        name = app_name + ':change_password'
        url = reverse(name)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_resolve_url_change_password(self):
        resolver = resolve('/accounts/change_password/')
        self.assertEqual(resolver.url_name, 'change_password')
        self.assertEquals(resolver.func, change_password)
"""
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))
"""