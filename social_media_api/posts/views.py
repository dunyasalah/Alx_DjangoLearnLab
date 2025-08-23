from rest_framework import generics, permissions
from rest_framework.response import Response
from posts.models import Post
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification

class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        feed_posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  # ده السطر المطلوب
        data = [{"id": post.id, "title": post.title, "content": post.content, "author": post.author.username, "created_at": post.created_at} for post in feed_posts]
        return Response(data)
class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked",
                target=post
            )
        return Response({"status": "liked"})

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        Like.objects.filter(user=request.user, post=post).delete()
        return Response({"status": "unliked"})