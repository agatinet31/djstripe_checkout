from django.urls import path

from item.views import StripeSessionIDView, item_checkout

app_name = "item"

urlpatterns = [
    path(
        "buy/<int:pk>/", StripeSessionIDView.as_view(), name="item_session_id"
    ),
    path("item/<int:id>/", item_checkout, name="item_checkout"),
]
