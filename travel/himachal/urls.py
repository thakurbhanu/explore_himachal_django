from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('explore/', views.BookListView.as_view(), name='explore'),
    path('contact/', views.contact, name='contact'),
    path('place/<int:pk>', views.BookDetailView.as_view(), name='place-detail'),
]
