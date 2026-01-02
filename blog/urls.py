from django.urls import path
from . import views


app_name = 'Журнал'

urlpatterns = [
    path('', views.post_list, name='post_list'), 
    path('/post/new/', views.add_post, name='add-post'),
    path('post/<int:pk>/edit/', views.post_edit, name='post-edit')
]