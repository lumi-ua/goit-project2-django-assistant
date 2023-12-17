from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Note, Tag


class NoteAppTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.tag = Tag.objects.create(name='Test Tag', author=self.user)
        self.note = Note.objects.create(name='Test Note', description='Test Description', author=self.user)
        self.note.tags.add(self.tag)

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'note_app/index.html')

    def test_tag_view(self):
        response = self.client.post(reverse('tag'), {'name': 'New Tag'})
        self.assertEqual(response.status_code, 302)  # 302 for redirect
        self.assertTrue(Tag.objects.filter(name='New Tag', author=self.user).exists())

    def test_note_view(self):
        response = self.client.post(reverse('note'), {'name': 'New Note', 'description': 'New Description', 'tags': [self.tag.id]})
        self.assertEqual(response.status_code, 302)  # 302 for redirect
        self.assertTrue(Note.objects.filter(name='New Note', description='New Description', author=self.user).exists())

    def test_detail_view(self):
        response = self.client.get(reverse('detail', args=(self.note.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'note_app/detail.html')
        self.assertIn('note', response.context)
        self.assertEqual(response.context['note'], self.note)

    def test_set_done_view(self):
        response = self.client.get(reverse('set_done', args=(self.note.id,)))
        self.assertEqual(response.status_code, 302)  # 302 for redirect
        self.assertTrue(Note.objects.get(pk=self.note.id).done)

    def test_delete_note_view(self):
        response = self.client.get(reverse('delete_note', args=(self.note.id,)))
        self.assertEqual(response.status_code, 302)  # 302 for redirect
        self.assertFalse(Note.objects.filter(pk=self.note.id).exists())

    def test_search_note_view(self):
        response = self.client.get(reverse('search_note') + '?q=Test')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'note_app/search_note.html')
        self.assertIn('notes', response.context)
        self.assertTrue(self.note in response.context['notes'])


# Run tests
# python manage.py test
