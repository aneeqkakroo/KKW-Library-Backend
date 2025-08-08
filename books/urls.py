from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # optional
    path('search/', views.search, name='search'),  # optional
    path('book/<int:pk>/', views.book_detail, name='book_detail'),  # optional
    path('upload/', views.upload_book, name='upload_book'),  # optional

    # ✅ API routes
    path('api/books/', views.EbookListCreateAPIView.as_view(), name='api_books'),
    path('api/books/<int:pk>/', views.EbookDetailAPIView.as_view(), name='api_book_detail'),
]
