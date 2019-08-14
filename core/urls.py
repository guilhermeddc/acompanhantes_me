from django.urls import path

from .views import index

urlpatterns = [
    path('', index, name='index'),
]

# {% url 'detail' slug=Client.slug %} or {{ Client.get_absolute_url }}
