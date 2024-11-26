from django.urls import path
from .views import translation, home

urlpatterns = [
    path('api/', translation.as_view(), name='API Endpoint'),
    path('', home, name = 'Home')
]