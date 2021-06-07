from flask import jsonify, render_template, redirect, url_for, request, flash, session
from contactbook.models import Contact_Book
from contactbook.serialization import Contact_Book_Schema
from contactbook import app
from contactbook import db
from contactbook.forms import FormValidation

# read


@app.route("/api/contacts", methods=['GET'])
def apiIndex():
    all_contacts = Contact_Book_Schema(many=True)
    contacts = Contact_Book.query.order_by(Contact_Book.id).all()
    output = all_contacts.dump(contacts)
    return jsonify({'Contacts': output})


@app.route("/api/search/<search>", methods=['GET'])
def apiSeach(search):
    all_contacts = Contact_Book_Schema(many=True)
    if '@' in search:
        contact = Contact_Book.query.filter(Contact_Book.email.contains(search)).all()
        output = all_contacts.dump(contact)
    else:
        contact = Contact_Book.query.filter(Contact_Book.name.contains(search)).all()
        output = all_contacts.dump(contact)
    return jsonify({"Contacts": output})

# Create


@app.route("/api/create_contact", methods=('GET', 'POST'))
def ApiCreateContact():
    print(request.form)
    form = FormValidation(request.form, meta={'csrf': False})
    if form.validate_on_submit():
        contact = Contact_Book()
        form.populate_obj(contact)
        db.session.add(contact)
        try:
            data = db.session.commit()
            return jsonify({'result': "success"}), 201
        except:
            db.session.rollback()
            jsonify({'Error': 'Give the right input'}), 404

    return jsonify({'Error': 'Already exist Or Wrong input'}), 404

# update


@app.route("/api/edit_contact/<id>", methods=('GET', 'POST'))
def apiEdit_contact(id):
    contact = Contact_Book.query.filter_by(id=id).first()
    # print(contact)
    form = FormValidation(obj=contact, meta={'csrf': False})
    if form.validate_on_submit():
        try:
            form.populate_obj(contact)
            db.session.add(contact)
            db.session.commit()
            return jsonify({'success': 'Saved successfully'}), 200
        except:
            db.session.rollback()
            return jsonify({'Error': 'Already Exist Or Wrong Input'}), 400
    else:
        return jsonify({'Error': 'Wrong field'}), 400

# delete


@ app.route("/api/contacts/delete", methods=('POST',))
def apiContacts_delete():
    try:
        d_id = request.form.get('id')
        contact = Contact_Book.query.filter_by(id=d_id).first()
        db.session.delete(contact)
        db.session.commit()
        return jsonify({'danger': 'Delete successfully'}), 302
    except:
        db.session.rollback()
        return jsonify({'Error': 'Id Not Found'}), 404
