from flask import flash, redirect, render_template, request, url_for
from market import app
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, SellForm
from market import db
from flask_login import login_user, logout_user, login_required, current_user
from market.forms import BuyForm


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market', methods=['GET', 'POST'])
@login_required
def market_page():
    buy_form = BuyForm()
    sell_form=SellForm()
    if request.method == 'POST':
        purchased_item = request.form.get('buy')
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(
                    f'Successfully Purchased : {{p_item_object.name}} for {{p_item_object.price}}$', category='info')
            else:
                flash(
                    f'Current Budget is insufficient to purchase the {p_item_object.name}!', category='danger')
            return redirect(url_for('market_page'))

    if request.method == 'GET':
        items = Item.query.filter_by(owner=None)
        owned_item=Item.query.filter_by(owner=current_user.id)
        return render_template('market.html', items=items,buy_form=buy_form,owned_item=owned_item,sell_form=sell_form)


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
        login_user(new_user)
        flash(f'Successfully created an account!You are know logged in as : {new_user.username}',category='success')
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
            flash(f'Successfully signed in as: {attempted_user.username}',category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and Password not matched.Please try again!',category='danger')
    return render_template('login.html',login_form=login_form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash('You have been logged out!',category='info')
    return redirect(url_for('home_page'))


# CROSS SITE REQUEST FORGERY