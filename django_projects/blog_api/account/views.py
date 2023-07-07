from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import action
from rest_framework.response import Response


from comment.serializers import CommentSerializer
from like.serializers import FavoriteSerializer
from posts.serializers import PostListLikeSerializer
from . import serializers
from dj_rest_auth.views import LogoutView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer


class CustomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated,)


class UserViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.UserListSerializer
        return serializers.UserDitailSerializer

    @action(['GET'], detail=True)
    def favorites(self, request, pk):
        user = self.get_object()
        fav_posts = user.favorites.all()
        serializer = FavoriteSerializer(fav_posts, many=True)
        from rest_framework.response import Response
        return Response(serializer.data, status=200)

    @action(['GET'], detail=True)
    def comments(self, request, pk=None):
        user = self.get_object()
        comments = user.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=200)

    @action(['GET'], detail=True)
    def liked_posts(self, request, pk=None):
        user = self.get_object()
        likes_all = user.likes.all()
        posts = [like.post for like in likes_all]
        serializer = PostListLikeSerializer(posts, many=True)
        return Response(serializer.data, status=200)

# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserListSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#
# class UserDetailView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserDitailSerializer
#     permission_classes = (permissions.IsAuthenticated,)
