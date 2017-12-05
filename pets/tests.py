from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase,APIClient
from rest_framework.authtoken.models import Token

from pets import views
from pets.models import Pet


class ViewTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
    	self.user = User.objects.create(email="test@exmaple.com", username="test")
    	self.user.set_password("password123")
    	self.user.save()
        self.token, created = Token.objects.get_or_create(user=self.user)
        self.token.save()

        url ='/user/pets/'
        data = { 'pet_type': 'D', 'name': 'Billabong', 'owner': self.user, 'birthday': '2017-11-11' }
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}
        response = self.client.post(url, data, {}, **header)
        self.assertEqual(response.status_code, 200)
        self.assertTrue( response.json() )      

   	
    def test_api_signup(self):
    	url = '/user/signup/'
    	data = {"email": "test1@gmail.com", "password": "password123", 'username': "test1"}
    	response = self.client.post(url, data, follow=True)
    	self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Successfully Created Your Account.')    	

    def test_api_signup_already_existing_user(self):
    	url = '/user/signup/'
    	data = {"email": "test@gmail.com", 
    			"password": "password123",
                "username": 'test'}
    	response = self.client.post(url, data, follow=True)
    	self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['non_field_errors'], ['Please enter a unique username'] )      

    def test_api_login_with_correct_credientials(self):
    	url = '/user/login/'
    	data = {"email": "test@exmaple.com", 
    		    "password": "password123"}
    	response = self.client.post(url, data, follow=True)
        self.token, created = Token.objects.get_or_create(user=self.user)
        self.token.save()
    	self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Successfully login.')

    def test_api_login_with_uncorrect_credientials(self):
        url = '/user/login/'
        data = {"email": "test@exmaple.com",
                        "password": 'UNKNOWNpassword'}
        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['login'], ['Unable to log in with provided credentials.'] )      

    def test_api_logout(self):
        url = '/user/logout/'
        data = { 'token': self.token } 
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}
        response = self.client.post(url,data, {}, **header)  
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'],"Successfully logout." )      

    def test_api_get_data(self):
        url = '/user/pets/'
        data = { } 
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}
        response = self.client.get(url, data, {}, **header)  
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['name'], 'Billabong')      

    def test_api_post_data(self):
        url = '/user/pets/'
        data = { 'pet_type': 'C', 'name': 'mypet', 'owner': self.user }
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}
        response = self.client.post(url, data, {}, **header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'mypet')      

    def test_api_update_data(self):
        url = '/user/pets/1/'
        data = { 'pet_type': 'D', 'name': 'mypet_dog', 'owner': self.user }
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}
        response = self.client.put(url, data, {}, **header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'mypet_dog')      

    def test_api_delete_data(self):
        url = '/user/pets/1/'
        data = {  }
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}
        response = self.client.delete(url, data, {}, **header)
        self.assertEqual(response.status_code, 200)
        import pdb; pdb.set_trace()    
        self.assertTrue( response.json()['message'],'Successfully Deleted.' )      

