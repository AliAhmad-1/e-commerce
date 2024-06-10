from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.views.i18n import set_language

urlpatterns = [
    path('i18n/',include('django.conf.urls.i18n')),
  
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('',include('shop.urls',namespace='shop')),
    path(_('cart/'),include('cart.urls',namespace='cart')),
    path(_('order/'),include('orders.urls',namespace='orders')),
    path(_('payment/'),include('payment.urls',namespace='payment')),
    path(_('coupons/'),include('coupons.urls',namespace='coupons')),
    
 
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
