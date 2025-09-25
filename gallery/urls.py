from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('category/<slug:slug>/', views.category_view, name='category'),
    path('image/<int:pk>/', views.image_detail, name='image_detail'),
    

]
