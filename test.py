from yookassa import Payment, Configuration
import uuid
Configuration.account_id = "205657"
Configuration.secret_key = "live_4eSjc0jOzCdLdPIhKKSFWU6RO0qItSSTP2CF88LcPwg"

if type(5) == int:
    print('fff')

payment = Payment.create({
    "amount": {
        "value": "600.00",
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
                "description": "Наименование товара 1",
                "quantity": "2.00",
                "amount": {
                    "value": "250.00",
                    "currency": "RUB"
                },
                "vat_code": "2",
                "payment_mode": "full_prepayment",
                "payment_subject": "commodity"
            },
            {
                "description": "Наименование товара 2",
                "quantity": "1.00",
                "amount": {
                    "value": "100.00",
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


print(payment.json())