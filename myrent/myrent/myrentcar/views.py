from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Car

# Create your views here.


# def index(request):
#     return HttpResponse("Hell, world, You're at the rent car index")


def cars(request):
    cars = Car.objects.all()
    print(cars)
    return render(request, 'myrentcar/cars.html', {'cars': cars})


def car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'myrentcar/car.html', {'car': car})