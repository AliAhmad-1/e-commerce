from django import forms
from django.utils.translation import gettext_lazy as _
class CartAddProductForm(forms.Form):
    PRODUCT_QUANTITY_CHOICE=[ (i,str(i)) for i in range(1,12)]
    quantity=forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICE, coerce=int, label=_('Quantity'))
    override=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput())