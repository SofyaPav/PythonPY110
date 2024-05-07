from django.shortcuts import render

from django.http import HttpResponse
import datetime


def datetime_view(request):
    if request.method == "GET":
        data = datetime.datetime.now()  # Написать, что будет возвращаться из данного представления
        return HttpResponse(data)

