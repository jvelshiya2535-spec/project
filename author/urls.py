from django.urls import path
from .views import create_author,get_author,updateauthor,delete_author,get_author_id
urlpatterns=[
    path('create/',create_author,name='create_author'),
    path('fetched/',get_author,name='get_author'),
    path('update/<int:pk>',updateauthor,name='updateauthor'),
    path('delete/<int:pk>',delete_author,name='delete_author'),
    path('get/<int:pk>',get_author_id,name='get_id')
]