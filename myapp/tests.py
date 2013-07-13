from django.test import TestCase
from myapp.models import Animal
from django.test.client import Client
class AnimalTestCase(TestCase):
	def setUp(self):
		Animal.objects.create(name="lion", sound="roar")
		Animal.objects.create(name="cat", sound="meow")
		self.c = Client()

	def test_animals_can_speak(self):
		"""Animals that can speak are correctly identified"""
		lion = Animal.objects.get(name="lion")
		cat = Animal.objects.get(name="cat")
		self.assertEqual(lion.speak(), 'The lion says "roar"')
		self.assertEqual(cat.speak(), 'The cat says "meow"')
#	def test_browser(self):
#		"""server test"""
#		response = self.c.get('http://127.0.0.1:8000/')
#		self.assertEqual(response.status_code, 200)
