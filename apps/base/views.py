"""Views for the base app"""

from django.shortcuts import render

def index(request):
    """ Default view for the root """
    return render(request, 'base/index.html',{'a':'2'})