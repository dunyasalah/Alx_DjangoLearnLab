from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from django.contrib.auth.models import User


class BookAPITestCase(APITestCase):
    def setUp(self):
        # إنشاء يوزر للتجربة
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        
        # إنشاء كتاب للتجربة
        self.book = Book.objects.create(title="Book 1", author="Author 1", price=10.50)
        
        # روابط الـ endpoints
        self.list_url = reverse("book-list")   # لازم يكون عندك ViewSet أو URL باسم ده
        self.detail_url = reverse("book-detail", args=[self.book.id])

    def test_get_books_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book.title)

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")
        data = {"title": "New Book", "author": "Author 2", "price": 15.00}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        data = {"title": "New Book", "author": "Author 2", "price": 15.00}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        self.client.login(username="testuser", password="testpass123")
        data = {"title": "Updated Title", "author": "Author 1", "price": 12.00}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
