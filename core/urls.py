from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import UserListView, test

urlpatterns = [
    path('', UserListView.as_view(), name='index'),
    path('test/', test, name='test'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# {% url 'detail' slug=Client.slug %} or {{ Client.get_absolute_url }}
