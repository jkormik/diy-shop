from django.contrib import admin
from .models import Category, Product, Favorite, Cart, CartItem, Order, OrderItem, HomepageBanner, HomepageBannerBottom

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'total_price', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('email', 'phone')

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'added_at')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'session_id', 'created_at')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'price', 'quantity')

@admin.register(HomepageBanner)
class HomepageBannerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not HomepageBanner.objects.exists()

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(HomepageBannerBottom)
class HomepageBannerBottomAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not HomepageBannerBottom.objects.exists()

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False
