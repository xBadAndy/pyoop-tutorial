from item import Item

item1 = Item("MyItem", 750)
print(item1.name)

item1.apply_increment(0.2)
item1.apply_discount()

# Getting an Attribute
print(item1)
