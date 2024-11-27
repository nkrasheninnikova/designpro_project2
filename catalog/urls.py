from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('account/', views.indexacc, name='profile'),
    path('signup/', views.signup, name='signup'),
]
