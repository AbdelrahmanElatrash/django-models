from django.test import TestCase
from .models import Snack
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.

class SnackModelTest(TestCase):

    def test_list_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user=get_user_model().objects.create_user(
            username='test',
            email='teas@email.com',
            password='1234'
        )
        cls.snack=Snack.objects.create(
            name="test snack" ,
            purchaser=cls.user , 
            description="test description"
        )


    def test_fields(self):
        self.assertIsInstance(self.snack.name , str)
        self.assertIsInstance(self.snack.description , str)

    def test_user_model(self):
        self.assertIsInstance(self.snack.purchaser, object )


    def test_detail_page_status_code(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')

    
    def test_detail_page_context(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        snack = response.context['snack']
        self.assertEqual(snack.name, "test snack")
        self.assertEqual(snack.description, "test description")
        self.assertEqual(snack.purchaser.username, "test")