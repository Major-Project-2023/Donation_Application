from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.views.decorators.csrf import csrf_exempt
from django.dispatch import receiver

@csrf_exempt
@receiver(valid_ipn_received)
def webhook(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        mc_gross = ipn_obj.mc_gross 
        payment_date = ipn_obj.payment_date
        payment_status = ipn_obj.payment_status
        first_name = ipn_obj.first_name
        print(f"{mc_gross},{payment_date},{payment_status},{first_name}")



    # print('this is hook')
    # print(ipn_obj)
    # return