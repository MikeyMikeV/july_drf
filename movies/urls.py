from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('first/', views.first_step, name= 'first_step'),
    path('second/<int:film_id>/', views.second_step, name= 'second_step'),
    path('third/<int:film_id>/', views.third_step, name= 'third_step'),
]
