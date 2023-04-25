from django.shortcuts import render
from .forms import paymentForm1, paymentForm2, paymentForm3, paymentFormAll
from yookassa import Payment, Configuration


# Create your views here.
def payment(request):
    if request.method == 'POST':
        form = paymentFormAll(request.POST)
        if form.is_valid() and form.has_changed():
            Configuration.account_id = "205657"
            Configuration.secret_key = "live_4eSjc0jOzCdLdPIhKKSFWU6RO0qItSSTP2CF88LcPwg"
            try:
                field_value = form.cleaned_data['field1']
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
                    "test": True
                })

                json = payment.json().replace('&quot;', '')
                return render(request, 'test.html', {'tuple1': json})

            except:
                print('error1')

            try:
                field_value = form.cleaned_data['field2']
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
                    "test": True
                })

                json = payment.json().replace('&quot;', '')
                return render(request, 'test.html', {'tuple1': json})
            except:
                print('error2')

            try:
                field_value = form.cleaned_data['field3']
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
                    "test": True
                })

                json = payment.json().replace('&quot;', '')
                return render(request, 'test.html', {'tuple1': json})
            except:
                print('error3')



    else:
        form = paymentFormAll()
        return render(request, 'payment.html', {'form': form})









