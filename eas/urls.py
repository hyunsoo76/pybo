from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'eas'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail', views.detail, name='detail'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)