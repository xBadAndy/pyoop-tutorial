from phone import Phone
from keyboard import Keyboard

item1 = Phone("jscPhone", 1000, 3)
item2 = Keyboard("jscKeyboard", 50, 3)

item1.apply_discount()
print(item1.price)

item2.apply_discount()
print(item2.price)