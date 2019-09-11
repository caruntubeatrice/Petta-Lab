from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import temp_1, temp_2, temp_3, temp_4, temp_5, temp_6, press_1, press_2, press_3, press_4, press_5, press_6

class Graph_home(TemplateView):
    template_name = 'graphs.html'

# Makes the pressure views
def plotPress(request, num, day):
    nr = int(num)
    d = int(day)
    if (nr == 1):
        data = press_1.objects.order_by("-time")[:d]
    elif (nr == 2):
        data = press_2.objects.order_by("-time")[:d]
    elif (nr == 3):
        data = press_3.objects.order_by("-time")[:d]
    elif (nr == 4):
        data = press_4.objects.order_by("-time")[:d]
    elif (nr == 5):
        data = press_5.objects.order_by("-time")[:d]
    elif (nr == 6):
        data = press_6.objects.order_by("-time")[:d]
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    return render(request, 'press.html', {'data': data,
                                         'len': data.count(),
                                         'num': num,})



# Makes the temperature graph views
def plotTemp(request, num, day):
    nr = int(num)
    d = int(day)
    if (nr == 1):
        data = temp_1.objects.order_by("-time")[:d]
    elif (nr == 2):
        data = temp_2.objects.order_by("-time")[:d]
    elif (nr == 3):
        data = temp_3.objects.order_by("-time")[:d]
    elif (nr == 4):
        data = temp_4.objects.order_by("-time")[:d]
    elif (nr == 5):
        data = temp_5.objects.order_by("-time")[:d]
    elif (nr == 6):
        data = temp_6.objects.order_by("-time")[:d]
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    return render(request, 'temp.html', {'data': data,
                                         'len': data.count(),
                                         'num': num,})







