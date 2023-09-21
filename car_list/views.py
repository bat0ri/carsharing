from django.shortcuts import render, redirect
from .models import Transport
from .models import Cart, CartItem
from django.db.models import F, Sum
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page


@cache_page(10)  # Кэширование
def car_list(request, transport_type='auto'):

    offers = Transport.objects.filter(type=transport_type)
    is_moderator = request.user.groups.filter(name='Модераторы').exists()

    count = len(offers)
    context = {
        'offers': offers,
        'count' : count,
        'is_moderator': is_moderator,
    }
    return render(request, 'car_list/car_list.html', context)


def offer_detail(request, offer_id):
    offer = get_object_or_404(Transport, id=offer_id)

    # Проверяем наличие транспорта в корзине
    in_cart = CartItem.objects.filter(transport=offer, cart__user=request.user).exists()
    num_visits = request.session.get(str(offer_id), 1)
    request.session[str(offer_id)] = num_visits + 1

    context = {
        'offer': offer,
        'in_cart': in_cart,
        'num_visits': num_visits
    }

    return render(request, 'car_list/offer.html', context)


def main_page(request):
    return render(request, 'car_list/main.html')


def cart_view(request):
    cart = Cart.objects.filter(user=request.user).first()
    items = cart.items.all() if cart else []

    total_price = 0

    if cart:
        total_price = cart.items.annotate(item_total=F('transport__price') * F('quantity')).aggregate(total=Sum('item_total'))['total']

    context = {
        'cart': cart,
        'price': total_price,
        'total': total_price + 995 if total_price is not None else 0,
        'items': items
    }
    response = render(request, 'car_list/cart.html', context)

    if not items:
        response.set_cookie('cart_empty', 'true')
    else:
        response.delete_cookie('cart_empty')

    return response


def add_to_cart(request, transport_id):
    transport = get_object_or_404(Transport, id=transport_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, transport=transport)

    if not item_created and not request.session.get('pause', True):
        cart_item.quantity += 1
        cart_item.save()
        request.session.set_expiry(60)
        request.session['pause'] = True

    transport.is_booked = True
    transport.save()

    response = redirect('cart')

    return response


def remove_from_cart(request, transport_id):
    transport = get_object_or_404(Transport, id=transport_id)
    cart = get_object_or_404(Cart, user=request.user)

    CartItem.objects.filter(cart=cart, transport=transport).delete()

    transport.is_booked = False
    transport.save()

    return redirect('cart')


def increase_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.quantity += 1
    item.save()
    return redirect('cart')


def decrease_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    return redirect('cart')


def payment_page(request):
    cart = Cart.objects.filter(user=request.user).first()
    items = cart.items.all() if cart else []

    # Вычисляем общую сумму, умножая цену аренды каждого автомобиля на его количество
    total_price = \
    cart.items.annotate(item_total=F('transport__price') * F('quantity')).aggregate(total=Sum('item_total'))[
            'total'] if cart else 0

    context = {
        'price': total_price,
        'total': total_price + 995,
    }

    return render(request, 'car_list/payment.html', context)


def add_page(request):
    if request.method == 'POST':
        type = request.POST['type']
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        capacity = request.POST['capacity']
        image = request.FILES['image']
        departure_time = request.POST['departure_time']
        arrival_time = request.POST['arrival_time']
        arenda = request.POST['arenda']

        transport = Transport.objects.create(
            type=type,
            name=name,
            description=description,
            price=price,
            capacity=capacity,
            image=image,
            departure_time=departure_time,
            arrival_time=arrival_time,
            arenda=arenda
        )
        transport.save()

        return redirect('add')

    return render(request, 'car_list/add.html')


def transport_delete(request, offer_id):
    transport = get_object_or_404(Transport, id=offer_id)

    if request.method == 'POST':
        transport.delete()
        transport_type = request.GET.get('transport_type', 'auto')
        return redirect('offers', transport_type=transport_type)

    return redirect('offer', offer_id=offer_id)


