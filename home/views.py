from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view returns the index.html page """

    return render(request, 'home/index.html')
