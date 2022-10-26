from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from comment.models import Comment
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from comment.serializers import CommentSerializer, CreateCommentSerializer
from user.serializers import UserSerializer
User = get_user_model()


class CommentsFromUserView(GenericAPIView):
    permission_classes = [IsAuthenticated, AllowAny]

    def get(self, request, *args, **kwargs):
        all_comments = Comment.objects.all()
        serializer = CommentSerializer(all_comments, many=True)
        comments_by_user = list()

        for counter in range(0, len(serializer.data)):
            if serializer.data[counter]['user'] == self.kwargs['user_id']:
                comments_by_user.append(serializer.data[counter])

        return Response(comments_by_user)


class CreateCommentView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CreateCommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user, review=self.kwargs['review_id'])

        return Response(serializer.data)


class DeleteCommentView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        specific_comment = Comment.objects.get(id=self.kwargs['comment_id'])
        specific_comment.delete()

        return Response("Comment deleted.")