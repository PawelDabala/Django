from django.urls import path

from . import views

app_name = 'myrentcar'
urlpatterns = [
    #ex: /cars/
    path('cars/', views.cars, name='cars'),
    #ex: /cars/5/
    path('<int:car_id>/', views.car, name='car')
]