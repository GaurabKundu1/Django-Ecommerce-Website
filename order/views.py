import json
import uuid

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from product.models import Product
from cart.carts import Cart, Coupon
from .forms import CheckoutForm
from .models import Order, OrderItem

# Create your views here.

class Checkout(LoginRequiredMixin, generic.View):
    login_url = reverse_lazy('login')
    
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form': form
        }
        return render(self.request, 'order/checkout.html', context)
    
    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            return JsonResponse({
                'success': True,
                'errors': None
            })
        else:
            return JsonResponse({
                'success': False,
                'errors': dict(form.errors)
            })
        

class SaveOrder(LoginRequiredMixin, generic.View):
    login_url = reverse_lazy('login')
    
    def post(self, *args, **kwargs):
        customer_information = json.loads(self.request.body)
        cart = Cart(self.request)
        coupon_id = cart.coupon
        user_cart = Cart(self.request).cart
        products = Product.objects.filter(id__in=list(user_cart.keys()))
        ordered_products = []

        for product in products:
            order_item = OrderItem.objects.create(
                product=product,
                price=product.price,
                quantity=user_cart[str(product.id)]['quantity'],
            )
            ordered_products.append(order_item)
        
        order = Order.objects.create(
            user=self.request.user,
            transaction_id=uuid.uuid4().hex,
            **customer_information
        )

        order.order_items.add(*ordered_products)

        if coupon_id:
            order.coupon = Coupon.objects.get(id=coupon_id)
            order.save()

        

        if float('%.2f' % cart.total()) != float(order.total):
            order.paid = False
            order.save()

        cart.clear()

        return JsonResponse({'success': True})
    

class Orders(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('login')
    model = Order
    template_name = 'order/orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)