from cgitb import html
from email.policy import HTTP
from http.client import HTTPResponse
from tkinter import Menu
from urllib.request import HTTPRedirectHandler
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(Request):


    #html = "<h1>INFJMC</h1> \n <hr> </hr> \n <p> Bienvenido a la página de la Facultad de Ingeniería de la Universidad Nacional de Ingeniería. </p> \n"
    #Menu = "<ul> <li><a href='{ % url 'docentes' %}'>DOCENTES</a></li> <li><a href='{ % url 'carreras' %}'>Carreras</a></li> </ul>"
    #contenido = "<hr><p>lorem</p>"
    #return HttpResponse(html + Menu + contenido)
    return render(Request, "core/home.html")
def carreras(Request):
    return HttpResponse("<h1>Carreras.</h1>")


def docentes(Request):
    return HttpResponse("<h1>Docentes.</h1>")

