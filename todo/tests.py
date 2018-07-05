from django.test import TestCase
from .models import TodoItem
from .forms import TodoForm


class Test(TestCase):

    def create_whatever(self, text="only a test"):
        return TodoItem.objects.create(text=text)

    def test_whatever_creation(self):
        w = self.create_whatever()
        self.assertTrue(isinstance(w, TodoItem))
        self.assertEqual(w.__str__(), w.text)

    def test_index(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_valid_form(self):
        w = TodoItem.objects.create(text='Foo')
        data = {'text': w.text}
        form = TodoForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        w = TodoItem.objects.create(text='')
        data = {'text': w.text}
        form = TodoForm(data=data)
        self.assertFalse(form.is_valid())
