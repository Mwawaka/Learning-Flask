from flask import render_template
from market import app
from market.models import Item
from market.forms import RegisterForm




@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items=Item.query.all()
    return render_template('market.html',items=items)


@app.route('/register')
def register_page():
    form=RegisterForm()
    if form.validate_on_submit():
        pass
    return render_template('register.html',form=form)