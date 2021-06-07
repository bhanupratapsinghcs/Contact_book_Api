from contactbook import db
from contactbook.models import Contact_Book
from contactbook import ma


class Contact_Book_Schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Contact_Book
        include_fk = True
