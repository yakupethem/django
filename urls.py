from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('authors',views.authors,name='authors'),
    path('books',views.books,name='books'),
    path('details/<int:authorId>',views.details,name='details')
]
