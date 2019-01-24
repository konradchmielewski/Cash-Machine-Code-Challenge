from django.test import TestCase
import random


class TestCashMachine(TestCase):

    def test_response(self):
        response = self.client.get('/')
        self.assertEquals(int(response.status_code), 200)

    def test_random_positive_number(self):
        random_number = random.randint(1, 10000)
        response = self.client.post('/', {'valueof': str(random_number)})
        self.assertEquals(int(response.status_code), 200)

    def test_negative_number(self):
        negative_number = -10
        response = self.client.post('/', {'valueof': str(negative_number)})
        self.assertEquals(int(response.status_code), 200)

    def test_string_value(self):
        string_value = "Test string."
        response = self.client.post('/', {'valueof': string_value})
        self.assertEquals(int(response.status_code), 200)

    def test_empty_string(self):
        string_value = ""
        response = self.client.post('/', {'valueof': string_value})
        self.assertEquals(int(response.status_code), 200)

