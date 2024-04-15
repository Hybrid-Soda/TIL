from rest_framework import serializers
from .models import Book, Review

class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('isbn',)

class ReviewListSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Review
        fields = ('book', 'content', 'score')
        read_only_fields = ('book',)

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('book',)

class ReviewPlusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('content', 'score')

class BookSerializer(serializers.ModelSerializer):
    review_set = ReviewPlusSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
