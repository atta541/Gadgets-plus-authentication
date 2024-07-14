

from django.urls import path
from .views import (
    LaptopListCreate, LaptopDelete,
    MobileListCreate, MobileDelete,
    LEDListCreate, LEDDelete,
    check_auth, login_page, logout_view, register_page,LaptopCreateView
)

urlpatterns = [
    path('api/addlaptops/', LaptopCreateView.as_view(), name='laptop-create'),

    path('api/laptops/', LaptopListCreate.as_view(), name='laptop-list-create'),
    path('api/laptops/<int:pk>/', LaptopDelete.as_view(), name='laptop-delete'),
    
    path('api/mobiles/', MobileListCreate.as_view(), name='mobile-list-create'),
    path('api/mobiles/<int:pk>/', MobileDelete.as_view(), name='mobile-delete'),
    path('api/leds/', LEDListCreate.as_view(), name='led-list-create'),
    path('api/leds/<int:pk>/', LEDDelete.as_view(), name='led-delete'),


    path('api/check-auth/', check_auth, name='check-auth'),
    path('api/login/', login_page, name='login'),
    path('api/logout/', logout_view, name='logout'),
    path('api/register/', register_page, name='register'),

]
