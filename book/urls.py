from django.urls import path
from .views import create_book,get_book,updatebook,delete_book,get_book_id,get_bookbyyear,get_bookbytitle,get_bookbyprice,get_bookbyrange,get_bookbyauthor
urlpatterns=[
    path('create/',create_book,name='create_book'),
    path('fetched/',get_book,name='get_book'),
    path('update<int:pk>',updatebook,name='updatebook'),
    path('delete<int:pk>',delete_book,name='delete_book'),
    path('get<int:pk>',get_book_id,name='get_id'),
    path('fetched/',get_book,name='get_book'),
    path('fetch/',get_bookbyyear,name='get_bookbyyear'),
    path('fetchs/',get_bookbytitle,name='get_bookbytitle'),
    path('fetd/',get_bookbyprice,name='get_bookbytitle'),
    path('fets/',get_bookbyrange,name='bookbyrange'),
    path('find/',get_bookbyauthor,name='get_bookbyauthor')
]