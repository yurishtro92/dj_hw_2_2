from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return redirect(reverse('bus_stations'))


with open('C:/Users/79803/PycharmProjects/pythonProject21/data-398-2018-08-30.csv', newline='',
          encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    bus_stations_list = []
    for row in reader:
        bus_stations_list.append(row)


def bus_stations(request):
    paginator = Paginator(bus_stations_list, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    try:
        bus_stations_on_page = paginator.page(page_number)
    except PageNotAnInteger:  # обработка кейса ввода произвольных данных вместо числа (номера) страницы
        bus_stations_on_page = paginator.page(1)
    except EmptyPage:  # обработка кейса перехода на несуществующую страницу
        bus_stations_on_page = paginator.page(paginator.num_pages)
    context = {
        'bus_stations': bus_stations_on_page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
