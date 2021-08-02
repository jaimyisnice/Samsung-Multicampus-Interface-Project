from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'my_page'
urlpatterns = [
    path('', views.my_page, name='my_page'),
    path('update/', views.update, name='update'),
    path('my_lecture/', views.my_lecture, name='my_lecture'),
    path('delete/', views.delete, name='delete')
]