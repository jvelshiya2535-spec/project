from django.urls import path
from .views import create_file,login_user,get_file,updatefile,delete_file,get_file_id

urlpatterns=[
    path('create/',create_file,name='create_file'),
    path('login/',login_user,name='login_user'),
    path('fetched',get_file,name='get_file'),
    path('update/<int:pk>',updatefile,name='updatefile'),
    path('delete/<int:pk>',delete_file,name='delete_file'),
    path('get/<int:pk>',get_file_id,name='get_id')
    ]
