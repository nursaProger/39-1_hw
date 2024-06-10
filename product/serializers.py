from rest_framework import serializers
from .models import Category, Product, Review, Tag


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'

    def get_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            return sum(review.stars for review in reviews) / len(reviews)
        return None



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def get_products_count(self, obj):
        return obj.product_set.count()

    class ProductSerializer(serializers.ModelSerializer):
        tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True, required=False)

        class Meta:
            model = Product
            fields = '__all__'

        def validate_tags(self, value):
            if not Tag.objects.filter(pk__in=value).exists():
                raise serializers.ValidationError("One or more tags do not exist.")
            return value



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'





