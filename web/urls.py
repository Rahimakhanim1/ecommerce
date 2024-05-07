from django.urls import path
from web.views import home

urlpatterns = [
    path('',home, name='home')
]
