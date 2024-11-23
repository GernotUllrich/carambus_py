from django.urls import path
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the home page!")

urlpatterns = [
    path('', home_view, name='home'),  # Define a view for the root URL
]
