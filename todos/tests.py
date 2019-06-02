# Import Dependencies
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from .models import Todo

# Implementing Test Cases to ensure that future updates will not break the system with TDD
class TodoTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
        username='testuser',
        email='test@email.com',
        password='secret'
    )

        self.todo = Todo.todos.create(
            title='A good title',
            description='Nice description content',
            creator=self.user,
            status='active'
        )

    def test_string_representation(self):
        todo = Todo(title='A sample title')
        self.assertEqual(str(todo), todo.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.todo.get_absolute_url(), '/todo/1/')

    def test_todo_content(self):
        self.assertEqual(f'{self.todo.title}', 'A good title')
        self.assertEqual(f'{self.todo.creator}', 'testuser')
        self.assertEqual(f'{self.todo.description}', 'Nice description content')

    def test_todo_list_view(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice description content')
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_todo_detail_view(self):
        response = self.client.get('/todo/1/')
        no_response = self.client.get('/todo/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'todo_detail.html')

    def test_todo_create_view(self): 
        response = self.client.post(reverse('create_todo'), {
        'title': 'New title',
        'description': 'New text',
        'creator': self.user,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')

    def test_todo_update_view(self): 
        response = self.client.post(reverse('todo_edit', args='1'), {'title': 'Updated title',
        'description': 'Updated text', 'status': 'active'
        })
        self.assertEqual(response.status_code, 302)

    def test_todo_delete_view(self): 
        response = self.client.get(
        reverse('todo_delete', args='1'))
        self.assertEqual(response.status_code, 200)