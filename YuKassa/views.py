from django.shortcuts import render
from .forms import paymentFormAll
from yookassa import Payment, Configuration
import json as JSon
import uuid



# Create your views here.
id = ''

def payment(request):
    global id
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
                        "type": "redirect",
                        "return_url": "http://185.154.194.38/ok/"
                    },
                    "receipt": {
                        "customer": {
                            "full_name": "Иванов Иван Иванович",
                            "phone": "79000000000",
                            "email": "724101@gmail.com"
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
                    "test": False
                })
                json_post = payment.json()
                json_js = json_post.replace('&quot;', '')
                print(json_js)
                data = json_post
                json_data = JSon.loads(data)
                payment_id = json_data['id']
                id = payment_id
                print(id)
                return render(request, 'test.html', {'tuple1': json_js})

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
                        "type": "redirect",
                        "return_url": "http://185.154.194.38/ok/"
                    },
                    "receipt": {
                        "customer": {
                            "full_name": "Иванов Иван Иванович",
                            "phone": "79000000000",
                            "email": "724101@gmail.com"
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
                    "test": False
                })

                json_post = payment.json()
                json_js = json_post.replace('&quot;', '')
                print(json_js)
                data = json_post
                json_data = JSon.loads(data)
                payment_id = json_data['id']
                id = payment_id
                return render(request, 'test.html', {'tuple1': json_js})
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
                        "type": "redirect",
                        "return_url": "http://185.154.194.38/ok/"
                    },
                    "receipt": {
                        "customer": {
                            "full_name": "Иванов Иван Иванович",
                            "phone": "79000000000",
                            "email": "724101@gmail.com",
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
                    "test": False
                })

                json_post = payment.json()
                json_js = json_post.replace('&quot;', '')
                print(json_js)
                data = json_post
                json_data = JSon.loads(data)
                payment_id = json_data['id']
                id = payment_id
                print(id)
                return render(request, 'test.html', {'tuple1': json_js})
            except:
                print('error3')



    else:
        form = paymentFormAll()
        return render(request, 'payment.html', {'form': form})

def ok(request):
    return render(request, 'ok.html')


def check(request):
    id
    Configuration.account_id = "205657"
    Configuration.secret_key = "live_4eSjc0jOzCdLdPIhKKSFWU6RO0qItSSTP2CF88LcPwg"
    payment1 = Payment.find_one(id)
    check_pay = payment1.json()
    return render(request, 'check.html', {'check': check_pay})









