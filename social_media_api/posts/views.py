from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification
from django.shortcuts import get_object_or_404
from rest_framework import status


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
        post = get_object_or_404(Post, pk=pk)  # ده اللي التشيكر طالباه
        user = request.user
        like, created = Like.objects.get_or_create(post=post, user=user)
        if created:
            # إنشاء Notification لو حبينا
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb='liked',
                target=post
            )
            return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'already liked'}, status=status.HTTP_200_OK)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        deleted, _ = Like.objects.filter(post=post, user=user).delete()
        if deleted:
            return Response({'status': 'unliked'}, status=status.HTTP_200_OK)
        return Response({'status': 'not liked yet'}, status=status.HTTP_400_BAD_REQUEST)