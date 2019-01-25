from django.test import TestCase
import random
from .views import get_notes_from_amount


class TestCashMachine(TestCase):

    def test_response(self):
        response = self.client.get('/')
        self.assertEquals(int(response.status_code), 200)

    def test_correct_positive_number(self):
        test_value = (random.randint(1, 100)) * 10
        expected_notes = get_notes_from_amount(test_value)
        response = self.client.post('/', {'input_value': test_value})
        self.assertEquals(response.context['notes'], str(expected_notes))
        self.assertEquals(int(response.status_code), 200)

    def test_incorrect_positive_value(self):
        test_value = (random.randint(1, 1000) * 2) - 1
        expected_response = "NoteUnavailableException"
        response = self.client.post('/', {'input_value': test_value})
        self.assertEquals(response.context['notes'], expected_response)
        self.assertEquals(int(response.status_code), 200)

    def test_negative_number(self):
        test_value = -10
        expected_response = "InvalidArgumentException"
        response = self.client.post('/', {'input_value': test_value})
        self.assertEquals(response.context['notes'], expected_response)
        self.assertEquals(int(response.status_code), 200)

    def test_string_value(self):
        test_value = "Type your test string here."
        expected_response = "InvalidArgumentException"
        response = self.client.post('/', {'input_value': test_value})
        self.assertEquals(response.context['notes'], expected_response)
        self.assertEquals(int(response.status_code), 200)

    def test_empty_string(self):
        test_value = ""
        expected_response = "[Empty Set]"
        response = self.client.post('/', {'input_value': test_value})
        self.assertEquals(response.context['notes'], expected_response)
        self.assertEquals(int(response.status_code), 200)

