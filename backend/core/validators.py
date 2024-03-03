from django.core.validators import RegexValidator, _lazy_re_compile
from django.utils.translation import gettext_lazy as _

simple_name_re = _lazy_re_compile(r"^[^\W\d_][\w \-()]+$")
validate_simple_name = RegexValidator(
    simple_name_re,
    _(
        "Enter a valid `name` value consisting of only letters, digit. "
        "and symbols _ ( )"
        "The first symbol only letter."
    ),
    "invalid",
)
