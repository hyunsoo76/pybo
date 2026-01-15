# eas/urls.py
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "eas"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:Request_id>/", views.detail, name="detail_r"),

    # (주의) detail은 Request_id 인자가 필요한 detail 뷰와 시그니처가 안 맞을 수 있어.
    # 필요 없으면 지우는 걸 추천. 일단 유지하려면 detail 뷰를 따로 만들거나 URL을 없애야 함.
    # path("detail", views.detail, name="detail"),

    path("Request/create/", views.Request_create, name="Request_create"),
    path("Request/create_24/", views.Request_create_24, name="Request_create_24"),
    path("Request/create/sangsin/<int:new_Request_id>/", views.Request_create_sangsin, name="Request_create_sangsin"),

    path("detail/update/<int:new_Request_id>/", views.detail_update, name="detail_update"),
    path("detail/okupdate/<int:new_Request_id>/", views.detail_okupdate, name="detail_okupdate"),
    path("detail/update2/<int:new_Request_id>/", views.detail_update2, name="detail_update2"),
    path("detail/okupdate2/<int:new_Request_id>/", views.detail_okupdate2, name="detail_okupdate2"),

    path("detail_modify/<int:new_Request_id>/", views.Request_modify, name="Request_modify"),

    path("monthly_holiday/", views.monthly_holiday, name="monthly_holiday"),
    path("monthly_holiday_r/<int:Request_id>/", views.monthly_holiday_r, name="monthly_holiday_r"),
    path("monthly_holiday_r/okupdate2/<int:new_Request_id>/", views.monthly_holiday_r_okupdate2, name="monthly_holiday_r_okupdate2"),
    path("monthly_holiday_r/update2/<int:new_Request_id>/", views.monthly_holiday_r_update2, name="monthly_holiday_r_update2"),

    path("account.html/", views.account, name="account"),

    path("nomal_approval/", views.nomal_approval, name="nomal_approval"),
    path("nomal_approval_r/<int:Request_id>/", views.nomal_approval_r, name="nomal_approval_r"),

    path("ds.html/", views.ds, name="ds"),

    # ✅ 자동완성 API
    path("api/vendor-suggest/", views.vendor_suggest, name="vendor_suggest"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
