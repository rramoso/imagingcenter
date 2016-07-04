from django.shortcuts import render
from django.views.generic import View


class Home(View):
	
	def get(self, request):

		return render(request, "index.html",{})

class About(View):
	
	def get(self, request):

		return render(request, "about.html",{})

class Services(View):
	
	def get(self, request):

		return render(request, "services.html",{})

class Service(View):
	
	def get(self, request):

		return render(request, "service.html",{})

class Patient(View):
	
	def get(self, request):

		return render(request, "patient.html",{})
