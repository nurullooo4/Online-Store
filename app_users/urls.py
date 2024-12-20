from django.urls import path

from app_users.views import (UserLogin,
                             user_logout,
                             UserRegistration,
                             CartView,
                             CartProductDeleteView,
                             update_cart_product
                             )

# app_name = 'app_users'

urlpatterns = [
    # http://127.0.0.1:8000/users/login/
    # http://localhost:8000/users/login/
    path('login/', UserLogin.as_view(), name='login'),
    # http://127.0.0.1:8000
    # http://127.0.0.1:8000
    path('logout/', user_logout, name='logout'),
    # http://127.0.0.1:8000/users/registration/
    # http://localhost:8000/users/registration/
    path('registration/', UserRegistration.as_view(), name='registration'),
    # http://127.0.0.1:8000/users/cart/
    # http://localhost:8000/users/cart/
    path('cart/', CartView.as_view(), name='cart'),
    path('cart_product_delete/<int:cart_product_id>/', CartProductDeleteView.as_view(), name='cart_product_delete'),
    path('update_cart_product/<int:cart_product_id>/<str:action>/', update_cart_product, name='update_cart_product'),
]
