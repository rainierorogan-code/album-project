from django.urls import path
from .views import AlbumListView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView

urlpatterns = [
    path('', AlbumListView.as_view(), name='album-list'),
    path('new/', AlbumCreateView.as_view(), name='album-create'),
    path('<int:pk>/edit/', AlbumUpdateView.as_view(), name='album-edit'),
    path('<int:pk>/delete/', AlbumDeleteView.as_view(), name='album-delete'),
]
