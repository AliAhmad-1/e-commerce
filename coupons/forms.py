from django import forms
from .models import Coupon
from django.utils.translation import gettext_lazy as _
class CouponApplyForm(forms.Form):
    code=forms.CharField(label=_('Coupon'))
