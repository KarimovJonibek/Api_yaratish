from django.urls import path
from .views import BookListApiView, BookDetailApiView, \
BookDeleteApiView, BookUpdateApiViwe, BookCreateApiView, BookMixedApiView


urlpatterns = [
    path('kitoblar/', BookListApiView.as_view()),
    path('kitob/<int:pk>/', BookDetailApiView.as_view()),
    path('kitob/delete/<int:pk>/', BookDeleteApiView.as_view()),
    path('kitob/update/<int:pk>/', BookUpdateApiViwe.as_view()),
    path('kitob/create/', BookCreateApiView.as_view()),
    path('kitob/mixed/<int:pk>/', BookMixedApiView.as_view())
]