# a = 12
# b = 4
# print(a + b)
# print(a.__add__(b))


class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

samsung = Kettle("Samsung", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, samsung.make, samsung.price))
# or
print(f"Models: {kenwood.make} = {kenwood.price}, {samsung.make} = {samsung.price}")

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, samsung))

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
"""

print(samsung.on)
samsung.switch_on()
print(samsung.on)

Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

print("*" * 80)

kenwood.power = 1.5
print(kenwood.power)
# print(samsung.power)

print("Swith to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)
print("Switch ´kenwood to gas")
kenwood.power_source = "gas"
print(kenwood.power_source)
print(samsung.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(samsung.__dict__)


