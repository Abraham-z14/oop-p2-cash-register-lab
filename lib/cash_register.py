#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Discount must be an integer between 0 and 100.
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        # Add the transaction cost to the running total.
        self.total += price * quantity

        # Store each individual item purchased.
        for _ in range(quantity):
            self.items.append(item)

        # Save transaction details so the most recent purchase can be voided.
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount

            print(
                f"After the discount, the total comes to "
                f"${self.total:g}."
            )
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()

        price = last_transaction["price"]
        quantity = last_transaction["quantity"]

        # Reverse the cost of the most recent transaction.
        self.total -= price * quantity

        # Remove every item that belonged to that transaction.
        for _ in range(quantity):
            self.items.pop()