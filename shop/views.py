from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Cart, CartItem, Favorite, HomepageBanner, HomepageBannerBottom

def index(request):
    categories = Category.objects.all()
    featured_products = Product.objects.filter(is_available=True)[:4]
    banner = HomepageBanner.objects.first()
    banner_bottom = HomepageBannerBottom.objects.first()
    return render(request, 'shop/index.html', {
        'categories': categories,
        'featured_products': featured_products,
        'banner': banner,
        'banner_bottom': banner_bottom
    })

def product_list(request):
    category_slug = request.GET.get('category')
    products = Product.objects.filter(is_available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        
    return render(request, 'shop/products.html', {
        'products': products,
        'categories': Category.objects.all()
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})

def search(request):
    query = request.GET.get('q', '')
    category_slugs = request.GET.getlist('category')
    sort = request.GET.get('sort', '')

    products = Product.objects.filter(is_available=True)

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    
    if category_slugs:
        products = products.filter(category__slug__in=category_slugs)

    # Sorting logic
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    else:
        products = products.order_by('-created_at')

    return render(request, 'shop/search.html', {
        'products': products,
        'categories': Category.objects.all(),
        'query': query,
        'active_categories': category_slugs,
        'current_sort': sort
    })

def contacts(request):
    return render(request, 'shop/contacts.html')

def terms(request):
    return render(request, 'shop/terms.html')

# --- Cart & Favorites (Basic implementation) ---

def cart_view(request):
    # Get or create cart for current user/session
    cart = None
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        session_id = request.session.session_key
        if not session_id:
            request.session.create()
            session_id = request.session.session_key
        cart = Cart.objects.filter(session_id=session_id).first()

    if not cart:
        return render(request, 'shop/cart.html', {'cart_items': [], 'total_price': 0})

    cart_items = cart.items.all().select_related('product')
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    return render(request, 'shop/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'cart': cart
    })

def add_to_cart(request, product_id):
    # This is kept for backward compatibility or if needed, 
    # but we'll implement a toggle for the new requirement.
    return redirect('cart')

def toggle_cart_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if not cart:
            cart = Cart.objects.create(user=request.user)
    else:
        session_id = request.session.session_key
        if not session_id:
            request.session.create()
            session_id = request.session.session_key
        cart = Cart.objects.filter(session_id=session_id).first()
        if not cart:
            cart = Cart.objects.create(session_id=session_id)

    cart_item = CartItem.objects.filter(cart=cart, product=product).first()
    
    if cart_item:
        cart_item.delete()
        status = 'removed'
        message = 'Товар удален из корзины'
    else:
        CartItem.objects.create(cart=cart, product=product)
        status = 'added'
        message = 'Товар добавлен в корзину'
    
    total_count = sum(item.quantity for item in cart.items.all())
        
    return JsonResponse({
        'status': status, 
        'message': message, 
        'total_count': total_count
    })

def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart')

def clear_cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        session_id = request.session.session_key
        cart = Cart.objects.filter(session_id=session_id).first()
    
    if cart:
        cart.items.all().delete()
        
    return redirect('cart')

def favorites_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'shop/favorites.html', {'favorites': favorites})

@login_required
def toggle_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    favorite = Favorite.objects.filter(user=request.user, product=product)
    
    if favorite.exists():
        favorite.delete()
        status = 'removed'
    else:
        Favorite.objects.create(user=request.user, product=product)
        status = 'added'
        
    return JsonResponse({'status': status})
