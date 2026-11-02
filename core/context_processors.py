from shop.models import Cart, CartItem
from django.conf import settings

def cart_count(request):
    count = 0
    cart_products = []
    favorite_products = []
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        # Get favorites for authenticated user
        from shop.models import Favorite
        favorites = Favorite.objects.filter(user=request.user)
        favorite_products = [f.product_id for f in favorites]
    else:
        session_id = request.session.session_key
        if session_id:
            cart = Cart.objects.filter(session_id=session_id).first()
    
    if cart:
        items = cart.items.all()
        count = sum(item.quantity for item in items)
        cart_products = [item.product_id for item in items]
        
    return {
        'cart_count': count, 
        'cart_products': cart_products,
        'favorite_products': favorite_products
    }
