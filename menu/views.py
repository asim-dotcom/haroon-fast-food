import json
from urllib.parse import quote

from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CheckoutForm
from .models import FoodItem
from .models import Order, OrderItem


def menu_list(request):
    food_items = FoodItem.objects.filter(
        is_available=True
    ).select_related("category")

    context = {
        "food_items": food_items,
        "checkout_form": CheckoutForm(),
    }

    return render(request, "menu/menu_list.html", context)


def checkout(request):
    if request.method != "POST":
        return redirect("menu_list")

    form = CheckoutForm(request.POST)
    if not form.is_valid():
        return render_menu_with_checkout(request, form)

    try:
        cart_items = json.loads(form.cleaned_data["cart_data"])
    except (TypeError, json.JSONDecodeError):
        form.add_error("cart_data", "Your cart data is invalid. Please try again.")
        return render_menu_with_checkout(request, form)

    if not isinstance(cart_items, list) or not cart_items:
        form.add_error("cart_data", "Your cart is empty.")
        return render_menu_with_checkout(request, form)

    quantities = {}
    for cart_item in cart_items:
        if not isinstance(cart_item, dict):
            form.add_error("cart_data", "Your cart contains an invalid item.")
            return render_menu_with_checkout(request, form)

        item_id = cart_item.get("id")
        quantity = cart_item.get("quantity")
        if (
            isinstance(item_id, bool)
            or not isinstance(item_id, int)
            or isinstance(quantity, bool)
            or not isinstance(quantity, int)
            or quantity < 1
        ):
            form.add_error("cart_data", "Your cart contains an invalid quantity.")
            return render_menu_with_checkout(request, form)
        quantities[item_id] = quantities.get(item_id, 0) + quantity

    food_items = FoodItem.objects.filter(
        id__in=quantities,
        is_available=True,
    )
    food_by_id = {item.id: item for item in food_items}
    if len(food_by_id) != len(quantities):
        form.add_error(
            "cart_data",
            "One or more items are no longer available. Please refresh your cart.",
        )
        return render_menu_with_checkout(request, form)

    order_lines = []
    subtotal = 0
    for item_id, quantity in quantities.items():
        food_item = food_by_id[item_id]
        line_total = food_item.price * quantity
        subtotal += line_total
        order_lines.append((food_item, quantity, line_total))

    with transaction.atomic():
        order = Order.objects.create(
            customer_name=form.cleaned_data["customer_name"],
            customer_phone=form.cleaned_data["customer_phone"],
            delivery_address=form.cleaned_data["delivery_address"],
            landmark=form.cleaned_data["landmark"],
            instructions=form.cleaned_data["instructions"],
            payment_method=form.cleaned_data["payment_method"],
            payment_timing=form.cleaned_data["payment_timing"],
            subtotal=subtotal,
            total=subtotal,
        )
        OrderItem.objects.bulk_create(
            [
                OrderItem(
                    order=order,
                    food_item=food_item,
                    item_name=food_item.name,
                    quantity=quantity,
                    unit_price=food_item.price,
                    line_total=line_total,
                )
                for food_item, quantity, line_total in order_lines
            ]
        )

    return redirect("order_confirmation", reference=order.reference)


def render_menu_with_checkout(request, form):
    food_items = FoodItem.objects.filter(
        is_available=True
    ).select_related("category")
    return render(
        request,
        "menu/menu_list.html",
        {"food_items": food_items, "checkout_form": form},
    )


def order_confirmation(request, reference):
    order = get_object_or_404(
        Order.objects.prefetch_related("items"),
        reference=reference,
    )
    message_lines = [
        "Order for Haroon Khan's Fast Food",
        f"Order reference: {order.reference}",
        f"Customer: {order.customer_name}",
        f"Phone: {order.customer_phone}",
        "",
        "Items:",
    ]
    message_lines.extend(
        f"- {item.item_name} x {item.quantity}: Rs. {item.line_total}"
        for item in order.items.all()
    )
    message_lines.extend(
        [
            "",
            f"Final total: Rs. {order.total}",
            "",
            "Please review and confirm this order.",
        ]
    )
    whatsapp_message = "\n".join(message_lines)
    whatsapp_url = (
        "https://wa.me/923305583858?text="
        + quote(whatsapp_message, safe="")
    )
    return render(
        request,
        "menu/order_confirmation.html",
        {"order": order, "whatsapp_url": whatsapp_url},
    )