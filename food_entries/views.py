from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import Entry


class EntryList(generic.ListView):
    model = Entry
    queryset = Entry.objects.filter(status=1).order_by('-created_on')
    template_name = 'base.html'


# def index(response, id):
#     return render(response, "base.html", {})


# def home(response):
#     return render(response, "home.html", {})
