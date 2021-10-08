
class Jets:
    model = None
    country = 0

    def __init__(self, name, country, quantity):
        self.name = name
        self.origin = country
        self.quantity = quantity



first_item= Jets ("F14", "USA", 87)
second_item= Jets ("SU33", "RUSSIA", 35)

total = first_item.quantity+second_item.quantity
print(total)

