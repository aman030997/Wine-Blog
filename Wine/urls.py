from django.urls import path
from . import views

urlpatterns=[
    path('',views.wine_list,name='wine_list'),
    path('wine/<int:pk>/', views.wine_detail, name='wine_detail'),
    path('wine/new/', views.wine_new, name='wine_new'),
    
]
