
from django.contrib import admin
from django.urls import path
from product.views import (
    CategoryListAPIView, CategoryDetailAPIView,
    ProductListAPIView, ProductDetailAPIView,
    ReviewListAPIView, ReviewDetailAPIView,
    ProductReviewListAPIView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/reviews/', ProductReviewListAPIView.as_view(), name='product-reviews-list'),
    path('api/v1/categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('api/v1/categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('api/v1/products/', ProductListAPIView.as_view(), name='product-list'),
    path('api/v1/products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('api/v1/reviews/', ReviewListAPIView.as_view(), name='review-list'),
    path('api/v1/reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
]
