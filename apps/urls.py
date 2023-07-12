from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('setting/hero/', views.hero_index, name='hero-index'),
    path('setting/hero/add/', views.hero_add, name='hero-add'),
    path('setting/hero/update/<int:_id>/', views.hero_update, name='hero-update'),
    path('setting/hero/delete/<int:_id>/', views.hero_delete, name='hero-delete'),
    path('icon/', views.icon, name='icon'),
    path('profile/', views.profile, name='profile'),
    path('tables/', views.table, name='tables'),
]
