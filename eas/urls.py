from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'eas'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:Request_id>/', views.detail),
    path('detail', views.detail, name='detail'),
    path('Request/create/', views.Request_create, name='Request_create'),
    path('detail_r/_dojang/<int:Request_id>/', views.detail_r_dojang, name='detail_r_dojang'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)