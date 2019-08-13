from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'miapp/index.html')

def pestaña(request):
	return render(request, 'miapp/pestaña.html')	

def equipo(request):
	return render(request, 'miapp/equipodocente.html')

def turing(request):
	return render(request, 'miapp/turing.html')
			