from .models import cart,cartitem
from .views import _cart_id



def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            car_t=cart.objects.filter(Cart_id=_cart_id(request))
            car_items=cartitem.objects.all().filter(Cart=car_t[:1])
            for cart_items in car_items:
                item_count += cart_items.quantity
        except cart.DoesNotExist:
            item_count=0
    return dict(item_count=item_count)