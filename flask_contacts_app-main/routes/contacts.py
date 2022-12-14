from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact
from utils.db import db

contacts = Blueprint('contacts', __name__)

'''
Blueprints: un blueprint permite orgnizar las rutas haciendolas mas descriptivas
a continuacion se muestra como se hace uso de blueprint. 
--> esta blue print se registra en el archivo app.py
'''


@contacts.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)


@contacts.route('/new', methods=['POST'])
def add():
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']

    new_contact = Contact(fullname, email, phone)

    db.session.add(new_contact)
    db.session.commit()
    flash('Contact added correctly')
    return redirect(url_for('contacts.index'))


@contacts.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        contact = Contact.query.get(id)
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']
        db.session.commit()

        flash('Contact updated correctly')
        return redirect(url_for('contacts.index'))

    contact = Contact.query.get(id)
    return render_template('update.html', contact=contact)


@contacts.route('/delete/<int:id>')
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contact deleted correctly')
    return redirect(url_for('contacts.index'))


@contacts.route('/about')
def about():
    pass
