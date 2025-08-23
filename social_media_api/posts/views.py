from rest_framework import generics, permissions
from rest_framework.response import Response
from posts.models import Post

class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        feed_posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  # ده السطر المطلوب
        data = [{"id": post.id, "title": post.title, "content": post.content, "author": post.author.username, "created_at": post.created_at} for post in feed_posts]
        return Response(data)
