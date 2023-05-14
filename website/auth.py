from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', text="Moeen logged in")

@auth.route('/logout')
def logout():
    return "<h1>Logout page</h1>"

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('email must be greater than 3 chars', category='error')
        elif len(firstName) < 2:
            flash('firstname must be greater than 1 chars', category='error')
        elif password1 != password2:
            flash('passwords not matching', category='error')
        elif len(password1) < 7:
            flash('passwords length error', category='error')
        else:
            flash('successfully registered', category='success')
            pass
            # addd user to db
    return render_template('signup.html')