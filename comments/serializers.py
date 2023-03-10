from rest_framework import serializers

from posts.public_serializers import PostPublicSerializer, UserPublicSerializer

from .models import Comment


class CommentListSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    detail_url = serializers.HyperlinkedIdentityField(
        view_name='comments-detail',
        lookup_field ='pk',
    )

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'text',
            'detail_url',
        )

    def to_representation(self, instance):
        self.context['request'] = self.context.get('request')
        return super().to_representation(instance)


class CommentDetailSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    post = PostPublicSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'post',
            'text',
        )
