from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'eas'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:Request_id>/', views.detail, name='detail_r'),
    path('detail', views.detail, name='detail'),
    path('Request/create/', views.Request_create, name='Request_create'),
    path('detail/update/<int:new_Request_id>/', views.detail_update, name='detail_update'),
    path('detail/okupdate/<int:new_Request_id>/', views.detail_okupdate, name='detail_okupdate'),
    path('detail/update2/<int:new_Request_id>/', views.detail_update2, name='detail_update2'),
    path('detail/okupdate2/<int:new_Request_id>/', views.detail_okupdate2, name='detail_okupdate2'),
    path('detail_modify/<int:new_Request_id>/', views.Request_modify, name='Request_modify'),
    path('monthly_holiday/', views.monthly_holiday, name='monthly_holiday'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)