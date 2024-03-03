from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from core.validators import validate_simple_name


class Item(BaseModel):
    """Модель продукции."""

    name = models.CharField(
        _("name"),
        max_length=150,
        validators=[MinLengthValidator(3), validate_simple_name],
        help_text=_("Required. 3-150 characters. Letters, digit."),
    )
    price = models.CharField(
        _("price"),
        unique=True,
        max_length=100,
        help_text=_("Required. 100 characters."),
    )
    description = models.TextField(
        _("description"),
        max_length=250,
        blank=True,
        null=True,
        help_text=_("Not required. Description for item."),
    )

    def __str__(self):
        return (
            f"name: {self.name} ("
            f"price: {self.price}, "
            f"description: {self.description})"
        )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("name",)
