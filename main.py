from customer import Address, Customer


a = Address()
c = Customer()
c.set_customer_address(a)
c.set_customer_name('mario')

c2 = Customer()
a2 = Address()
c2.set_customer_address(a2)

c2.set_json(c.get_json())

print(c2.__dict__)


