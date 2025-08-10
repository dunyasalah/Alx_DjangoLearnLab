from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# ✅ عرض كل الكتب
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # متاح للجميع

# ✅ عرض كتاب واحد
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # متاح للجميع

# ✅ إنشاء كتاب جديد
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # لازم تسجيل دخول

# ✅ تعديل كتاب
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # لازم تسجيل دخول

# ✅ حذف كتاب
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # لازم تسجيل دخول
