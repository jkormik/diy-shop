from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="Слаг")
    image = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name="Изображение баннера")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория")
    name = models.CharField(max_length=200, verbose_name="Название товара")
    slug = models.SlugField(unique=True, verbose_name="Слаг")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение")
    is_available = models.BooleanField(default=True, verbose_name="В наличии")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites', verbose_name="Пользователь")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')
        verbose_name = "Избранное"
        verbose_name_plural = "Избранное"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь")
    session_id = models.CharField(max_length=100, null=True, blank=True, verbose_name="ID сессии")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return f"Корзина {self.id}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', verbose_name="Корзина")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    class Meta:
        verbose_name = "Позиция в корзине"
        verbose_name_plural = "Позиции в корзине"

    def get_total_price(self):
        return self.product.price * self.quantity

class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('processing', 'В обработке'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('cancelled', 'Отменен'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Пользователь")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    address = models.TextField(verbose_name="Адрес доставки")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая стоимость")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ #{self.id} - {self.email}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name="Заказ")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена на момент покупки")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    class Meta:
        verbose_name = "Позиция заказа"
        verbose_name_plural = "Позиции заказа"

class HomepageBanner(models.Model):
    image = models.ImageField(upload_to='banners/', verbose_name="Изображение баннера")
    title = models.CharField(max_length=255, default="Ручная работа, вдохновлённая природой", verbose_name="Заголовок")
    subtitle = models.TextField(default="Уникальные изделия с вышивкой, созданные с любовью для вашего уюта и вдохновения.", verbose_name="Подзаголовок")
    button_text = models.CharField(max_length=100, default="Перейти к каталогу", verbose_name="Текст кнопки")
    button_url = models.CharField(max_length=255, default="/products/", verbose_name="Ссылка кнопки")

    class Meta:
        verbose_name = "Главный баннер"
        verbose_name_plural = "Главный баннер"

    def __str__(self):
        return f"Баннер: {self.title}"

class HomepageBannerBottom(models.Model):
    image = models.ImageField(upload_to='banners/', verbose_name="Изображение баннера")
    title = models.CharField(max_length=255, default="Творчество в каждой детали", verbose_name="Заголовок")
    subtitle = models.TextField(default="Мы создаём изделия, которые сохраняют тепло рук и вдохновляют на уют в повседневной жизни. Каждая нить, каждый стежок — это история, рассказанная с любовью к природе и искусству.", verbose_name="Подзаголовок")
    button_text = models.CharField(max_length=100, default="Узнать больше", verbose_name="Текст кнопки")
    button_url = models.CharField(max_length=255, default="/contacts/", verbose_name="Ссылка кнопки")

    class Meta:
        verbose_name = "Главный баннер внизу"
        verbose_name_plural = "Главный баннер внизу"

    def __str__(self):
        return f"Нижний баннер: {self.title}"
