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
    path('detail/update/<int:new_Request_id>/', views.detail_update, name='detail_update'),
    path('detail/okupdate/<int:new_Request_id>/', views.detail_okupdate, name='detail_okupdate'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)