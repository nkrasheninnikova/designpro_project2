from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('account/', views.indexacc, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('request/', views.requests, name="requests"),
    path('request/add/', views.request_add, name="request_add"),
    path('request/delete/<int:pk>/', views.request_delete, name="request_delete"),
    path('request/delete/confirm/<int:pk>/', views.request_delete_confirm, name="request_delete_confirm"),
    path('request/done/change/<int:pk>/', views.request_done_change, name="request_done_change"),
    path('request/work/change/<int:pk>/', views.request_work_change, name="request_work_change"),
    path('categories/', views.categories, name="categories"),
    path('category/create/', views.category_create, name="category_create"),
    path('category/delete/<int:pk>/', views.category_delete, name="category_delete"),
]
