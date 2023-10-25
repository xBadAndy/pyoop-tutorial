import csv

# Parent class
class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    
    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.__name = name # add __ to beginning of attribute name to make it private (inaccessible outside of class)
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)
    
    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name

    # (Instance) methods pass in the instance as the first argument (self)
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price

    # Class metods pass in the class as the first argument (cls)
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    # Static methods do not send class or instance as an argument
    # Treat like a normal function and pass in whatever parameters are needed
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        # use self.__class__.__name__ to access name of child class used to create instance
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
