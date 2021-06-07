from contactbook.models import db, Contact_Book
from faker import Faker


fake = Faker('en_US')
db.drop_all()
db.create_all()

for num in range(100):
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    contact = Contact_Book(name=name, email=email, phone_number=phone)
    db.session.add(contact)

for num in range(17):
    name = "Aere"
    email = fake.email()
    phone = fake.phone_number()
    contact = Contact_Book(name=name, email=email, phone_number=phone)
    db.session.add(contact)
db.session.commit()
