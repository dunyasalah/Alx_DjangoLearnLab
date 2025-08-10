from django.db import models
from datetime import datetime

# Author model: يمثل كاتب واحد ويمكن أن يكون له عدة كتب
class Author(models.Model):
    name = models.CharField(max_length=255)  # اسم الكاتب

    def __str__(self):
        return self.name

# Book model: يمثل كتاب له عنوان، سنة النشر، وكاتب مرتبط
class Book(models.Model):
    title = models.CharField(max_length=255)  # عنوان الكتاب
    publication_year = models.IntegerField()  # سنة النشر
    author = models.ForeignKey(
        Author,
        related_name='books',  # للوصول للكتب المرتبطة بالكاتب
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
