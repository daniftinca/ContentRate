from django.http import HttpResponse
from django.shortcuts import render


def index(response):
    return render(response, "home.html")


def login(response):
    return render(response, "login.html")


def register(response):
    return render(response, "register.html")
