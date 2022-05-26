from flask import flash, redirect, render_template, url_for
from market import app, db
from market.models import Item, User
from market.forms import RegisterForm


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email_address=form.email_address.data,
            password_hash=form.password1.data
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(
                f'There was an error in creating the User: {err_msg}', category='danger')

    return render_template('register.html', form=form)
