"""Обьектно ориентиованное программирование"""
"Полиморфизм"

class PaymentMethod:
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f"Сумма {amount}, Оплачивается по кредитной карте"
    
class PayPal(PaymentMethod):
    def pay(self, amount):
        return f"Сумма {amount}, Оплачивается по Paypal"
    
class BankTransfer(PaymentMethod):
    def pay(self, amount):
        return f"Сумма {amount}, Оплачивается по банковскому переводу"
    
payments = [CreditCard(), PayPal(), BankTransfer()]

for payment in payments:
    print(payment.pay(input("Введите сумму: ")))