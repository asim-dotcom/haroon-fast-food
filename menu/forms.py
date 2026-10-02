from django import forms

from .models import Order


class CheckoutForm(forms.Form):
    customer_name = forms.CharField(max_length=150, label="Your name")
    customer_phone = forms.CharField(max_length=30, label="Phone number")
    delivery_address = forms.CharField(
        label="Delivery address",
        widget=forms.Textarea(attrs={"rows": 3}),
    )
    landmark = forms.CharField(max_length=200, required=False)
    instructions = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 3}),
    )
    payment_method = forms.ChoiceField(
        choices=Order.PaymentMethod.choices,
        label="Payment method",
    )
    payment_timing = forms.ChoiceField(
        choices=Order.PaymentTiming.choices,
        label="Payment timing",
    )
    cart_data = forms.CharField(widget=forms.HiddenInput)

    def clean_customer_phone(self):
        phone = self.cleaned_data["customer_phone"].strip()
        if len(phone) < 7:
            raise forms.ValidationError("Enter a valid phone number.")
        return phone
