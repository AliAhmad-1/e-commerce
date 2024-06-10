from celery import shared_task
from django.core.mail import send_mail,EmailMessage
from .models import Order
from django.conf import settings
from io import BytesIO
import weasyprint
from django.template.loader import render_to_string
@shared_task
def order_created(order_id):
    """ 
       Task to send an e-mail notification when an order is    successfully created.    
    """ 
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
        f'You have successfully placed an order.' \
        f'Your order ID is {order.id}.' 
    email = EmailMessage(subject,message,settings.EMAIL_HOST_USER,[order.email]) 
    html = render_to_string('pdf.html', {'order': order})
    out=BytesIO()
    stylesheets=[weasyprint.CSS('static/css/style.css')]
    weasyprint.HTML(string=html).write_pdf(out,stylesheets=stylesheets)
    email.attach_file(f'order_{order.id}.pdf',out.getvalue(),'application/pdf')
    email.send()
    
