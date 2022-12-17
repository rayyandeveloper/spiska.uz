from django.urls import path
from api.class_based import *
from api.function_based import *

urlpatterns = [
    path('shop/', ShopAPIView.as_view()),
    path('product/', ProductAPIView.as_view()),
    path('eproduct/', EProductAPIView.as_view()),
    path('user/', UserAPIView.as_view()),
    path('promocode/', PromocodeAPIView.as_view()),

    path('diamond/', diamond),

    path('regions/', regions),
    path('districts/', districts),
    
    path('geo/', geo),
        
    path('change-owner/', change_owner),
    path('like/', like),
    path('check-like/', check_like),
    path('check-barcode/', check_barcode),
    path('add-member/', shop_add_member),
    path('add-phone-number/', add_phone_number),
    path('add-admin/', shop_add_admin),
    path('report/', report),
    
    path('update-currency/', update_dollar_currency),
    
]


# s2023hop ning pul birligi almashtirilsa o'sha shopning hamma mahsulotlarini pul birligi o'zgartirilsin
 