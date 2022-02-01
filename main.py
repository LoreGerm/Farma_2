from customer import Address, Customer
import json

a = Address()
c = Customer()
c.set_customer_address(a)
c.set_customer_name('mario')

c2 = Customer()

c2.set_json(c.get_json())

print(c2.__dict__)


