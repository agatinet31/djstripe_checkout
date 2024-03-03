from django.shortcuts import get_object_or_404, render
from rest_framework.generics import RetrieveAPIView

from item.models import Item
from item.serializers import SessionIDSerializer
from payments.settings.base import STRIPE_PUBLIC_KEY


class StripeSessionIDView(RetrieveAPIView):
    """View-функция SessionID для выбранного товара."""

    queryset = Item
    serializer_class = SessionIDSerializer


def item_checkout(request, id):
    """View-функция Checkout формы."""
    item = get_object_or_404(Item, pk=id)
    context = {
        "item": item,
        "pk_api_key": STRIPE_PUBLIC_KEY,
    }
    return render(request, "items/checkout.html", context)
