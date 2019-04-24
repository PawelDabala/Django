from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Car, Client

# Create your views here.


# def index(request):
#     return HttpResponse("Hell, world, You're at the rent car index")


def cars(request):
    cars = Car.objects.all()
    return render(request, 'myrentcar/cars.html', {'cars': cars})


def car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'myrentcar/car.html', {'car': car})

def clients(request):
    clients = Client.objects.all()
    return render(request,'myrentcar/clients.html', {'clients': clients})

def client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'myrentcar/client.html', {'client': client})

# @csrf_exempt
def client_add(request):
    print("tutaj print", request.method)
    if request.method == "GET":
        return render(request, 'myrentcar/client_add.html')
    elif request.method == "POST":
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        print(name)
        print(last_name)
        Client.objects.create(name=name, last_name=last_name)
        return HttpResponseRedirect(reverse('myrentcar:clients'))




