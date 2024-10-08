from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import logout

from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.auth import get_user_model

from app_users.forms import UserRegistrationForm
from app_main.models import Cart


User = get_user_model()


class UserLogin(LoginView):
    template_name = 'auth/login.html'
    extra_context = {
        'is_auth': True,
    }

    def get_success_url(self):
        return self.request.POST.get('next')

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET' and request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class UserRegistration(CreateView):
    template_name = 'auth/registration.html'
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    extra_context = {
        'is_auth': True,
    }

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET' and request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


def user_logout(request):
    logout(request)
    return redirect('home')


class CartView(ListView):
    template_name = 'cart.html'
    context_object_name = 'cart_products'

    def get_queryset(self):
        return self.request.user.cart_set.all()


class CartProductDeleteView(DeleteView):
    model = Cart
    pk_url_kwarg = 'cart_product_id'
    success_url = reverse_lazy('cart')


def update_cart_product(request, cart_product_id, action):
    cart_product = get_object_or_404(Cart, pk=cart_product_id)

    if request.method == 'POST':
        if action == 'increment':
            cart_product.quantity += 1
        elif action == 'decrement' and cart_product.quantity > 1:
            cart_product.quantity -= 1
        cart_product.save()

    return redirect('cart')
