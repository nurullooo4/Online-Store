from django.urls import path

from app_main.views import (home_page,
                            product_detail,
                            add_to_cart
                            )

# app_name = 'app_main'

urlpatterns = [
    # http://127.0.0.1:8000/
    # http://localhost:8000/
    path('', home_page, name='home'),
    # http://127.0.0.1:8000/detail/id/
    # http://localhost:8000/detail/id/
    path('detail/<int:product_id>/', product_detail, name='detail'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
   ]
