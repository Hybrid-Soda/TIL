from rest_framework import serializers
from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


# 단일 데이터용
class ArticleSerializer(serializers.ModelSerializer):

	class Meta:
		model = Article
		fields = '__all__'