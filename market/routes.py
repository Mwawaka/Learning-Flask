from flask import flash, redirect, render_template, url_for
from market import app
from market.models import Item, User
from market.forms import RegisterForm,LoginForm
from market import db
from flask_login import login_user

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
            password=form.password1.data
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(
                f'There was an error in creating a User: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/login',methods=['GET','POST'])
def login_page():
    login_form=LoginForm()
    if login_form.validate_on_submit():
        attempted_user=User.query.filter_by(username=login_form.user_login.data).first()
        if attempted_user and attempted_user.check_password(attempted_password=login_form.password_login.data):
            login_user(attempted_user)
            flash(f'Successfully signed in as:{attempted_user.username}',category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and Password not matched.Please try again!',category='danger')
    return render_template('login.html',login_form=login_form)
