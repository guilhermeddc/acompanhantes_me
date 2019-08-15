from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import UserListView

urlpatterns = [
    path('', UserListView.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# {% url 'detail' slug=Client.slug %} or {{ Client.get_absolute_url }}
