from django.test import TestCase
from django.urls import reverse
from .models import Account


class HomePageTests(TestCase):

    url = 'accounts'
    
    def test_home_page_status_code(self):
        response = self.client.get(reverse(self.url))
        self.assertEquals(response.status_code, 200)
    
    def test_view_url_by_name(self):
        response = self.client.get(reverse(self.url))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse(self.url))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get(reverse(self.url))
        self.assertContains(response, '<table style="border-spacing: 10px">')

class CoreTests(TestCase):

    url = 'accounts'

    def setUp(self):
        Account.objects.create(
            website = 'testwebsite1.org',
            username = 'testuser1',
            email = 'testemail1@email.com',
            password = '126516SA136',
            description = 'test description'
        )
        Account.objects.create(
            website = 'testwebsite2.org',
            username = 'testuser2',
            email = 'testemail2@email.com',
            password = '723257725725',
            description = 'test description'
        )
        Account.objects.create(
            website = 'testwebsite3.org',
            username = 'testuser3',
            email = 'testemail3@email.com',
            password = 'asda136537',
            description = 'test description'
        )

    def test_text_content(self):
        account = Account.objects.get(id=1)
        expected_username = f'{account.username}'
        expected_email = f'{account.email}'
        expected_password = f'{account.password}'
        self.assertEquals(expected_username, 'testuser1')
        self.assertEquals(expected_email, 'testemail1@email.com')
        self.assertEquals(expected_password, '126516SA136')

    def test_account_view(self):
        response = self.client.get(reverse(self.url))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser2')
        self.assertContains(response, 'asda136537')


