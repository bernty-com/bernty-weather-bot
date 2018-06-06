from django.test import TestCase

from accounts.forms import SignUpForm


class SignUpFormTest(TestCase):

    def test_signup_form_email_field_label(self):
        form = SignUpForm()
        self.assertTrue(form.fields['email'].label is None or form.fields['email'].label == 'Адрес электронной почты')

    def test_signup_form_email_field_help_text(self):
        form = SignUpForm()
        self.assertEqual(
            form.fields['email'].help_text,
            'На адрес электронной почты будет отправлен запрос на подтверждение.'
        )


# OK python manage.py test accounts.tests.test_forms.SignUpFormTest.test_signup_form_email_field_help_text --keepdb
"""
    def test_renew_form_date_in_past(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        form_data = {'renewal_date': date}
        form = RenewBookForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_renew_form_date_too_far_in_future(self):
        date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
        form_data = {'renewal_date': date}
        form = RenewBookForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_renew_form_date_today(self):
        date = datetime.date.today()
        form_data = {'renewal_date': date}
        form = RenewBookForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_renew_form_date_max(self):
        date = timezone.now() + datetime.timedelta(weeks=4)
        form_data = {'renewal_date': date}
        form = RenewBookForm(data=form_data)
        self.assertTrue(form.is_valid())
"""
