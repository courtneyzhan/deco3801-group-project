from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='diary-home'),     # path('', views.home, name='diary-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), #pk primary key, int integer
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='diary-about'),
]
