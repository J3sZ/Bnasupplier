from django.urls import path
from .views import BnasupplierInfo

urlpatterns = [
    path("",BnasupplierInfo.as_view(), name = "home" ),
] 