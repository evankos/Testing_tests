"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from polls.models import Animal
from django.test.client import Client
import urllib2
import urllib
import ast
import subprocess
class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class AnimalTestCase(TestCase):
	def setUp(self):
		Animal.objects.create(name="lion", sound="roar")
		Animal.objects.create(name="cat", sound="meow")
		values = {'username' : 'dev','password' : '123456'}
		self.datas = urllib.urlencode(values)
		global false,null
		false = False
		null = None
		self.c = Client()
	def hitFormPost(self,url):
		req = urllib2.Request(url,self.datas)
		return urllib2.urlopen(req)

	def test_animals_can_speak(self):
		"""Animals that can speak are correctly identified"""
		lion = Animal.objects.get(name="lion")
		cat = Animal.objects.get(name="cat")
		self.assertEqual(lion.speak(), 'The lion says "roar"')
		self.assertEqual(cat.speak(), 'The cat says "meow"')
	def test_browser(self):
		"""server test"""
		response = self.c.get('http://127.0.0.1:8000/polls/')
		self.assertEqual(response.status_code, 200)
	def test_remote(self):
		"""remote connection"""
		response = urllib2.urlopen('http://www.google.com/')
		#print response.read()
		self.assertTrue('google' in response.read())
	def test_login(self):
		"""Login test"""
		# Send HTTP POST request
		#req = urllib2.Request('http://moodeettesting.herokuapp.com/person/signin', self.datas)
		response = self.hitFormPost('http://moodeettesting.herokuapp.com/person/signin')
		string = response.read()
		print string
		#can not parse with eval
		#eval('string = {"last_status": null, "is_followed": false, "is_available": false, "authentication": {"secret": "574ee3e9fd3ccf76c7da2a693a7e36e66b3bb516", "key": "test"}, "surname": "", "id": "173", "username": "test", "profile_pic": "http://s3.amazonaws.com/moodeetphotos/photos/130201184942.584.jpg", "name": ""}')
		#authentication =  ast.literal_eval(string)
		self.authentication = string[string.find('"secret":') + 11:string.find('",',string.find('"secret":') + 11)]
 		print 'AUTHENTICATION: '+self.authentication
		self.assertTrue(len(self.authentication)>3)
		cmd='curl -v -X GET -H "Authorization: OAuth oauth_consumer_key='+ self.authentication +'" http://moodeet.herokuapp.com/api/moodeet/mood/'
		#with open('/home/evan/Desktop/cmd.res','w') as fout: 
		subprocess.call(cmd,shell=True)
	#def test_mood(self):
	#	if (len(self.authentication)>3) :
			

















		
