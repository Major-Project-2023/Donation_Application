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

    # if ipn_obj.payment_status == ST_PP_COMPLETED:
    #     mc_gross = ipn_obj.mc_gross 
    #     payment_date = ipn_obj.payment_date
    #     payment_status = ipn_obj.payment_status
    #     first_name = ipn_obj.first_name
    #     payer_email = ipn_obj.payer_email
    #     ngo_name = ipn_obj.item_name
    #     receiver_email = ipn_obj.receiver_email
    #     mc_currency = ipn_obj.mc_currency
    #     payment_type = ipn_obj.payment_type
    #     user = User.objects.get(username=ipn_obj.custom)

        

    #     print(f"{mc_gross}\n{payment_date}\n{payment_status}\n{first_name}\n{payer_email}\n{receiver_email}\n{ngo_name}\n{mc_currency}\n{payment_type}\n{User}")
    #     transaction = Transaction()
    #     transaction.sender = user,
    #     transaction.receiver = ngo_name,
    #     transaction.sender_paypal_email = payer_email,
    #     transaction.receiver_paypal_email = receiver_email,
    #     transaction.date = payment_date,
    #     transaction.amount = mc_gross,
    #     transaction.currency = mc_currency,
    #     transaction.payment_status = payment_status,
    #     transaction.mode_of_payment = payment_type,

    #     transaction.save()

