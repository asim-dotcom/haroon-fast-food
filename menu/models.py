import uuid

from django.db import models

# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="items"
    )
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="food/", blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    class PaymentMethod(models.TextChoices):
        CASH = "cash", "Cash"
        EASYPAISA = "easypaisa", "Easypaisa"
        JAZZCASH = "jazzcash", "JazzCash"

    class PaymentTiming(models.TextChoices):
        ON_DELIVERY = "on_delivery", "Pay on delivery"
        ADVANCE = "advance", "Advance payment"

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        CONFIRMED = "confirmed", "Confirmed"
        PREPARING = "preparing", "Preparing"
        READY = "ready", "Ready"
        OUT_FOR_DELIVERY = "out_for_delivery", "Out for delivery"
        DELIVERED = "delivered", "Delivered"
        CANCELLED = "cancelled", "Cancelled"

    reference = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    customer_name = models.CharField(max_length=150)
    customer_phone = models.CharField(max_length=30)
    delivery_address = models.TextField()
    landmark = models.CharField(max_length=200, blank=True)
    instructions = models.TextField(blank=True)
    payment_method = models.CharField(
        max_length=20,
        choices=PaymentMethod.choices,
    )
    payment_timing = models.CharField(
        max_length=20,
        choices=PaymentTiming.choices,
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    subtotal = models.PositiveIntegerField()
    delivery_charge = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Order {self.reference}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
    )
    food_item = models.ForeignKey(
        FoodItem,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="order_items",
    )
    item_name = models.CharField(max_length=150)
    quantity = models.PositiveIntegerField()
    unit_price = models.PositiveIntegerField()
    line_total = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.item_name}"