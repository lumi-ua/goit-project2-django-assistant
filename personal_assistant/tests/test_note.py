# Create your tests here.
import unittest

from django.test import Client
from ..noteapp.forms import NoteForm

class NoteNewTestCase(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    def test_post_valid_form(self):
        # Testing when the request.method is "POST" and the form is valid
        response = self.client.post('/your_app/note_new/', {
            'title': 'Test Title',
            'content': 'Test Content',
            'tags': ['tag1', 'tag2']
        })
        self.assertEqual(response.status_code, 302)  # Check if the response is a redirect

    def test_post_invalid_form(self):
        # Testing when the request.method is "POST" and the form is invalid
        response = self.client.post('/your_app/note_new/', {
            'title': 'Test Title',
            'content': '',  # Invalid form data, missing required field
            'tags': ['tag1', 'tag2']
        })
        self.assertEqual(response.status_code, 200)  # Check if the response is a success

    def test_get_request(self):
        # Testing when the request.method is not "POST"
        response = self.client.get('/your_app/note_new/')
        self.assertEqual(response.status_code, 200)  # Check if the response is a success

if __name__ == '__main__':
    unittest.main()