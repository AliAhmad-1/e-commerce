from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

app_name='coupons'

urlpatterns = [
    path(_('apply/'), views.coupon_apply, name='apply'), 
]
