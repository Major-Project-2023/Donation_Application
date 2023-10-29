from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.views.decorators.csrf import csrf_exempt
from django.dispatch import receiver
from .models import Transaction
from django.contrib.auth.models import User

@csrf_exempt
@receiver(valid_ipn_received)
def webhook(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        transaction = Transaction.objects.create(
            sender=User.objects.get(username=ipn_obj.custom),
            receiver=ipn_obj.item_name,
            sender_paypal_email=ipn_obj.payer_email,
            receiver_paypal_email=ipn_obj.receiver_email,
            date=ipn_obj.payment_date,
            amount=ipn_obj.mc_gross,
            currency=ipn_obj.mc_currency,
            payment_status=ipn_obj.payment_status,
            mode_of_payment=ipn_obj.payment_type,
        )
        print(f"{ipn_obj.item_name}\n{ipn_obj.receiver_email}\n")
        # Save the Transaction instance
        transaction.save()
        
            #   \n{first_name}\n{payer_email}\n{receiver_email}\n{ngo_name}\n{mc_currency}\n{payment_type}\n{User}")