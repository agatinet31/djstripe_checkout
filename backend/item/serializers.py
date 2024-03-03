from rest_framework import serializers
from stripe._error import StripeError
from stripe.checkout import Session as StripeSession

from core.exceptions import UnavailableStripeService
from item.models import Item
from payments.settings.base import SUCCESS_URL


class SessionIDSerializer(serializers.ModelSerializer):
    """Сериалайзер SessionID, получаемого для продукта из Stripe."""

    session_id = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ("session_id",)

    def get_session_id(self, item):
        try:
            session_id = StripeSession.create(
                success_url=SUCCESS_URL,
                mode="payment",
                line_items=[
                    {
                        "price": item.price,
                        "quantity": 1,
                    }
                ],
            )["id"]
            return session_id
        except (StripeError, KeyError, OSError) as exc:
            raise UnavailableStripeService from exc
