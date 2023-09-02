from django.shortcuts import render
from django.http import HttpResponse
import json
import random

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")

def home_page(request):
    return render(request,"index.html")

def task(request):
    with open('myapp/kdramas.json', 'r') as file:
        kdramas = json.load(file)
    random_kdrama = random.choice(kdramas)
    context = {'kdrama': random_kdrama}
    return render(request, 'task.html', context)



