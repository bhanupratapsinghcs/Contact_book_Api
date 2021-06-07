from flask import jsonify, render_template, redirect, url_for, request, flash, session
from contactbook.models import Contact_Book
from contactbook import app
from contactbook import db
from contactbook.forms import FormValidation


@app.route("/")
def index():
    return redirect(url_for('contacts'))


# post method
@app.route("/create_contact", methods=('GET', 'POST'))
def create_contact():
    form = FormValidation()
    if form.validate_on_submit():
        contact = Contact_Book()
        form.populate_obj(contact)
        db.session.add(contact)
        try:
            db.session.commit()
            flash('Contact created correctly', 'success')
            return redirect(url_for('contacts'))
        except:
            db.session.rollback()
            flash('Enter Correct Email Id or Email already Exist.', 'danger')

    return render_template('pages/create_contact.html', form=form)


#  post method
@app.route("/edit_contact/<id>", methods=('GET', 'POST'))
def edit_contact(id):
    contact = Contact_Book.query.filter_by(id=id).first()
    form = FormValidation(obj=contact)
    if form.validate_on_submit():
        try:
            form.populate_obj(contact)
            db.session.add(contact)
            db.session.commit()
            flash('Saved successfully', 'success')
        except:
            db.session.rollback()
            flash('Error update contact.', 'danger')
    return render_template(
        'pages/edit_contact.html',
        form=form)

# get Method


@app.route('/contacts', methods=['GET'], defaults={"page": 1})
@app.route("/contacts/<int:page>")
def contacts(page):
    page = page
    per_page = 20
    contacts = Contact_Book.query.order_by(Contact_Book.name).paginate(page, per_page, error_out=False)
    return render_template('pages/contacts.html', contacts=contacts), 200


# post method
@app.route('/search', methods=['GET', 'POST'], defaults={"page": 1})
@app.route("/search/<int:page>", methods=['GET', 'POST'])
def search(page):
    per_page = 10
    if request.method == 'POST':
        print(request.form.get("search"))
        search =  request.form.get("search") # request.form.to_dict()['search'].strip()
        session['search'] = request.form.get('search')
        # if request.form.get("search"):
        #     search = request.form.get("search")
        #     print(search)
        if search == "":
            return redirect(url_for('contacts'))
        elif '@' in search:
            contacts = Contact_Book.query.filter(Contact_Book.email.contains(search)).paginate(page, per_page, error_out=False)
            return render_template('pages/SearchResult.html', contacts=contacts)
        else:
            contacts = Contact_Book.query.filter(Contact_Book.name.contains(search)).order_by(Contact_Book.name).paginate(page, per_page, error_out=False)
            return render_template('pages/SearchResult.html', contacts=contacts, search=search)
    search = session.get('search', None)
    contacts = Contact_Book.query.filter(Contact_Book.name.contains(search)).order_by(Contact_Book.name).paginate(page, per_page, error_out=False)
    return render_template('pages/SearchResult.html', contacts=contacts)


# delete method
@ app.route("/contacts/delete", methods=('POST',))
def contacts_delete():
    try:
        contact = Contact_Book.query.filter_by(id=request.form['id']).first()
        db.session.delete(contact)
        db.session.commit()
        flash('Delete successfully.', 'danger')
    except:
        db.session.rollback()
        flash('Error delete  contact.', 'danger')

    return redirect(url_for('contacts'))


@ app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('pages/404.html'), 404
