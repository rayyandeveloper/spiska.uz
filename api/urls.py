from django.urls import path
from api.class_based import *
from api.function_based import *

urlpatterns = [
    path('shop/', ShopAPIView.as_view()),
    path('product/', ProductAPIView.as_view()),
    path('user/', UserAPIView.as_view()),
    path('promocode/', PromocodeAPIView.as_view()),

    path('diamond/', diamond),

    path('regions/', regions),
    path('districts/', districts),

    path('geo/', geo),

    path('check-barcode/', check_barcode),

    path('chat-list/', chat_list),
    path('messages/', messages),
    path('send-message/', send_message),
    path('find-or-create/', get_or_create),


    path('change-owner/', change_owner),
    path('like/', like),
    path('check-like/', check_like),
    path('add-member/', shop_add_member),
    path('add-admin/', shop_add_admin),
    path('report/', report),
]
