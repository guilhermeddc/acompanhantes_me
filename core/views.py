from django.shortcuts import render
from django.views.generic import ListView
from .models import User


class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'pages/home_page.html'


def test(request):
    return render(request, 'signup-page.html')

# profile-page.html
