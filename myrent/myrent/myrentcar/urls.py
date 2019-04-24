from django.urls import path

from . import views

app_name = 'myrentcar'
urlpatterns = [
    #ex: /cars/
    #path('cars/', views.cars, name='cars'),
    path('cars/', views.CarsView.as_view(), name='cars'),
    #ex: /cars/5/
    path('cars/<int:pk>/', views.CarView.as_view(), name='car'),
    # path('cars/<int:car_id>/', views.car, name='car'),
    #ex: /clients/
    path('clients/', views.clients, name='clients'),
    #ex: /client/3/
    path('clients/<int:client_id>', views.client, name='client'),
    #ex: /clients/add/
    path('clients/add', views.client_add, name='client_add')
]