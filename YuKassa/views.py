from django.shortcuts import render
from .forms import paymentForm1, paymentForm2, paymentForm3, paymentFormAll
from yookassa import Payment, Configuration


# Create your views here.
def payment(request):
    if request.method == 'POST':
        form1 = paymentForm1(request.POST)
        form2 = paymentForm2(request.POST)
        form3 = paymentForm3(request.POST)
        Configuration.account_id = "205657"
        Configuration.secret_key = "live_4eSjc0jOzCdLdPIhKKSFWU6RO0qItSSTP2CF88LcPwg"
        if form1.is_valid() and form1.has_changed():
            field_value = form1.cleaned_data['field']
            tuple1 = (field_value)
            payment = Payment.create({
                "amount": {
                    "value": f"{int(tuple1)}.00",
                    "currency": "RUB"
                },
                "payment_method_data": {
                    "type": "sbp"
                },
                "confirmation": {
                    "type": "qr"
                },
                "receipt": {
                    "customer": {
                        "full_name": "Иванов Иван Иванович",
                        "phone": "79000000000"
                    },
                    "items": [
                        {
                            "description": "Наименование товара ",
                            "quantity": "1.00",
                            "amount": {
                                "value": f"{int(tuple1)}.00",
                                "currency": "RUB"
                            },
                            "vat_code": "2",
                            "payment_mode": "full_prepayment",
                            "payment_subject": "commodity"
                        }
                    ]
                },
                "capture": True,
                #"test": True
            })

            json = payment.json().replace('&quot;', '')
            return render(request, 'test.html', {'tuple1': json})


    else:
        form1 = paymentForm1()
        form2 = paymentForm2()
        form3 = paymentForm3()
        return render(request, 'payment.html', {'form1': form1, 'form2': form2, 'form3': form3})










