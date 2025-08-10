from rest_framework import generics, filters
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # التشيكر بيدور عليهم كده
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Book.objects.all()
    serializer_class = BookSerializer
    # فلترة
    filterset_fields = ['title', 'author', 'publication_year']
    
    # بحث
    search_fields = ['title', 'author']
    
    # ترتيب
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # ترتيب افتراضي
