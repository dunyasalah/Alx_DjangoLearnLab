# api/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)         # اسم الكتاب
    author = models.CharField(max_length=255)        # اسم المؤلف
    price = models.DecimalField(max_digits=5, decimal_places=2)  # سعر الكتاب

    def __str__(self):
        return self.title
