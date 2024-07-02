from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Post, Comment, Category

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        # fields = ['body', 'owner']
        fields = ['id', 'body', 'owner', 'post']

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'owner', 'posts']

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # comments = CommentSerializer(many=True, read_only=True)
    comments  = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner', 'comments', 'categories']
    
    def get_comments(self, obj):
        comments = obj.comments.all()
        return [{'Comment': comment.body, 'owner':{"id": comment.owner.id,"name" : comment.owner.username}} for comment in comments]



class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # comments = CommentSerializer(many=True, read_only=True)
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'comments', 'categories']
    
    def get_comments(self, obj):
        comments = obj.comments.all()
        return [{'Comment': comment.body, 'post': comment.post.id} for comment in comments]