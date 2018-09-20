from django.urls import path
from catalog import views

urlpatterns = [
        path('', views.index, name='index'),
        path('book/', views.AuthorListView.as_view(), name='books'),
        path('authors/', views.AuthorListView.as_view(), name='authors'),
]
