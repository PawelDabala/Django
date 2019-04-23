from django.urls import path

from . import views

app_name = 'myrentcar'
urlpatterns = [
    #ex: /cars/
    path('cars/', views.cars, name='cars'),
    #ex: /cars/5/
    path('cars/<int:car_id>/', views.car, name='car'),
    #ex: /clients/
    path('clients/', views.clients, name='clients'),
    #ex: /client/3/
    path('clients/<int:client_id>', views.client, name='client')
]