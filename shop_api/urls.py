
from django.contrib import admin
from django.urls import path
from product.views import (
    CategoryListAPIView, CategoryDetailAPIView,
    ProductListAPIView, ProductDetailAPIView,
    ReviewListAPIView, ReviewDetailAPIView,
    ProductReviewListAPIView,
    CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView,
    ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView,
    ReviewListCreateAPIView, ReviewRetrieveUpdateDestroyAPIView
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
    path('api/v1/categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('api/v1/categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),

    path('api/v1/products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('api/v1/products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),

    path('api/v1/reviews/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('api/v1/reviews/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-detail'),
]
