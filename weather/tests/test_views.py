from django.test import TestCase

# Run:
# python manage.py test weather.tests --keepdb 
# or
# python manage.py test weather.tests --keepdb --verbosity 2

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from weather.models import City, Country

class CityListViewTest(TestCase):

    def setUp(self):
        #Создание двух пользователей
        test_user1 = User.objects.create_user(username='testuser1', password='12345') 
        test_user1.save()
        test_user2 = User.objects.create_user(username='testuser2', password='12345') 
        test_user2.save()

    @classmethod
    def setUpTestData(cls):
        #Create 23 cities for pagination tests
        number_of_city = 23
        for city_num in range(number_of_city):
            City.objects.create(
                city_id=100 + int(city_num),
                name='Town %s' % city_num, 
                local_name='Городок %s' % city_num,
                coord_lon=0.0 + city_num * 2,
                coord_lat=0.0 + city_num * 3,
                country_id='RU',
            )
    
# OK
    def test_index_page_is_available(self):
        """
        Проверка доступности домашней страницы
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
# OK
    def test_redirect_if_not_logged_in_using_function(self):
        """
        Проверка перенаправления незалогиненного пользователя
        на форму аутенфикации 
        """
        resp = self.client.get(reverse('city_list'))
        self.assertRedirects(resp, '/accounts/login/?next=/citylist/')

# OK
    def test_login_and_redirection(self):
        """
        Проверка редиректа на главную после аутенфикации
        """
        response = self.client.post('/accounts/login/', {'username': 'testuser1', 'password': '12345'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

        response = self.client.post(reverse('accounts:login'), {'username': 'testuser1', 'password': '12345'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

# OK python manage.py test weather.tests.test_views.CityListViewTest.test_login_and_search_city --keepdb
    def test_login_and_search_city(self): 
        """
        Проверка для залогиненного пользователя
        работопоспобности поиска со страницы со списком городов
        Проверка работы пагинатора. 
        """
        resp = self.client.post('/accounts/login/', {'username': 'testuser1', 'password': '12345'})
        resp = self.client.get(reverse('city_list'),{'city':'Городок'})
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['city_lists']) == 20)
        
        #Get second page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('city_list'), {'city':'Городок','page':2})
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['city_lists']) == 3)


# OK python manage.py test weather.tests.test_views.CityListViewTest.test_redirect_to_404_if_not_logged --keepdb
    def test_redirect_to_404_if_not_logged(self):
        """
        Проверка выдачи ошибки 404 для незалогиненного пользователя
        при попытке прямой ссылки 
        """
        resp = self.client.get('/abcd/')
        self.assertEqual(resp.status_code, 404)
        

# ОК python manage.py test weather.tests.test_views.CityListViewTest.test_logged_in_uses_correct_template --keepdb
    def test_logged_in_uses_correct_template(self):
        """
        Ввод пользователя и пароля
        Проверка действительности залогиненности 
        Проверка правильности использования шаблона
        """
        login = self.client.login(username='testuser1', password='12345')
        resp = self.client.get(reverse('city_list'))
        
        #Проверка что пользователь залогинился
        self.assertEqual(str(resp.context['user']), 'testuser1')
        #Check that we got a response "success"
        self.assertEqual(resp.status_code, 200)

        #Проверка того, что мы используем правильный шаблон
        self.assertTemplateUsed(resp, 'weather/city_list.html')

# ОК python manage.py test weather.tests.test_views.CityListViewTest.test_login_and_logout --keepdb
    def test_login_and_logout(self):
        """
        Проверка логина и логаута
        """
        login = self.client.login(username='testuser1', password='12345')
        resp = self.client.get('/')
        
        #Проверка что пользователь залогинился
        self.assertTrue('user' in resp.context, True)           
        self.assertEqual(str(resp.context['user']), 'testuser1')
        #Check that we got a response "success"
        self.assertEqual(resp.status_code, 200)

        logout = self.client.logout()
        self.assertTrue('user' in resp.context, False)           
