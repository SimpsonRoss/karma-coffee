from django.db import models
from django.urls import reverse
from datetime import date, timedelta
from django.contrib.auth.models import User

ROAST = (
    ('L', 'Light'),
    ('M', 'Medium'),
    ('D', 'Dark'),
)

ORDER_STATUS = (
    ('C', 'Cart'),           # Order not yet completed
    ('P', 'Paid'),        # Order completed, payment pending
    ('S', 'Shipped'),        # Order shipped
    ('D', 'Delivered'),      # Order delivered
)

RATING = (
    (5, '5'),
    (4, '4'),
    (3, '3'),
    (2, '2'),
    (1, '1')
)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    origin = models.CharField(max_length=100)
    flavour = models.CharField(max_length=100)
    roast = models.CharField(
        max_length=1,
        choices=ROAST,
        default=ROAST[0][0]
    )
    image = models.ImageField(upload_to='product_images', blank=True)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'product_id': self.id})


# Ross - I'll use the customers order as the cart, until it's paid for, then update the status to pending..
class Order(models.Model):
    date = models.DateField('order date', auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(
        max_length=1, choices=ORDER_STATUS, default=ORDER_STATUS[0][0])
    session_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'Order #{self.id} - {self.get_status_display()}'

    # def get_absolute_url(self):
    #     return reverse('order_detail', kwargs={'order_id': self.id})

    def get_total(self):
        return sum(item.product.price * item.quantity for item in self.orderitem_set.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def get_total_item_price(self):
        return self.product.price * self.quantity


class Review(models.Model):
    purchase_date = models.DateField('Purchased Date', default=date.today() - timedelta(days=7))
    review_date = models.DateField('Review Date', default=date.today)
    content = models.TextField(max_length=250)
    rating = models.IntegerField(
        choices=RATING,
        default=RATING[0]
    )

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Purchased Date: {self.purchase_date} / Review Date: {self.review_date} / Product: { self.product.name } / "
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'product_id': self.product.id})

    class Meta:
        ordering = ['-purchase_date']
