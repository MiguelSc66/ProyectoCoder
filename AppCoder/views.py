from django.shortcuts import render
from calendar import c
from django.http import HttpResponse
from django.template import Template,  Context
from AppCoder.models import Family3
# Create your views here.
def Family(request):

	mama = Family3(nombre = "Ivana", edad = 48, fechaNac="1974-06-19")
	mama.save()
	papa = Family3(nombre = "Miguel", edad = 50, fechaNac="1972-03-26")
	papa.save()
	hermana = Family3(nombre = "Guadalupe", edad = 23, fechaNac="1999-05-06" )
	hermana.save()
	
	miHtml = open("C:/Users/Equipo/Desktop/trabajo django/ProyectoCoder/AppCoder/plantilla/family20.html")
	
	plantilla = Template(miHtml.read())
	
	miHtml.close()

	miContexto = Context()

	documento = plantilla.render(miContexto)
	
	return render(request, "family20.html",{"mama":mama,"papa":papa,"hermana":hermana})