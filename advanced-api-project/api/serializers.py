from rest_framework import serializers
from datetime import datetime
from .models import Author, Book

# Serializer لكتاب واحد
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # كل الحقول

    # تحقق مخصص للتأكد أن سنة النشر ليست في المستقبل
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Serializer لكاتب مع تضمين الكتب المرتبطة به
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested Serializer

    class Meta:
        model = Author
        fields = ['name', 'books']
