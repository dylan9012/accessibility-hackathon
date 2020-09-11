from flask import Flask, render_template, request, redirect, session, url_for

# import MySQLdb

app = Flask(__name__)
wsgi_app = app.wsgi_app
app.secret_key = 'e471e07eb0c2977afd4f398907cb78f8'

exampleUser = ["1", "Dylan Barker", "18", "Vision impairment", "E3 3NR", "Disabled", "dylanbarker59@gmail.com", "male",
               "07756756382", "destiny1"]


# def create_connection():
# return MySQLdb.connect(
# host='dylan9012.mysql.pythonanywhere-services.com',
# user='dylan9012',
# password='destiny1',
# db='dylan9012$WebApp',
# cursorclass=MySQLdb.cursors.Dictcursor
# )

class Account:
    matches = []


@app.route('/')
def index():
    if "email" in session:
        return redirect(url_for('dashboard'))
    return render_template('one/index.html')


@app.route('/about')
def about():
    return render_template('one/about.html')


@app.route('/contact')
def contact():
    team = ["Dylan Barker: dylanbarker59@gmail.com | King's College London ",
            "Eyuael Berhe: eyuael.berhe@gmail.com | Warwick University",
            "Isaac Addo: isaacaddo1714@gmail.com | King's College London",
            "Muhriz Tauseef: muhriztauseef82@gmail.com | King's College London"]
    return render_template('one/contact.html', team=team)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        entries = []
        name = request.form.get("name")
        age = request.form.get("age")
        number = request.form.get("number")
        gender = request.form.get("gender")
        email = request.form.get("email")
        password = request.form.get("password")
        postcode = request.form.get("postcode")
        role = request.form.get("role")
        s_d = request.form.get("speciality_or_disabled")
        entries.extend((name, age, number, gender, email, password, postcode, role, s_d))
        for i in entries:
            if not i or i == "Select":
                error = "Please fill in all fields"
                return render_template('one/signup.html', error=error, name=name, user_age=age, number=number, s_d=s_d,
                                       gender=gender, email=email, postcode=postcode, role=role)
        # with connection().cursor as cur:
        # signup_query = """INSERT INTO Account (Name, Age, Needs_or_Specialty, Location, Carer_or_client, Email,
        # Gender, Phone_number, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        # var_tuple = (name, age, s_d, postcode, role, email, gender, number, password)
        # cur.execute(signup_query, var_tuple)
        # cur.commit()

        success = "Sign up has succeeded, please login"
        return render_template('one/login.html', success=success)
    return render_template('one/signup.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        entries = []
        email = request.form.get("email")
        password = request.form.get("password")
        entries.extend((email, password))
        for i in entries:
            if not i:
                error = "Please fill in all fields"
                return render_template('one/login.html', error=error, email=email)
        # with connection().cursor as cur:
        # login_query = """SELECT Password, Email
        #                       FROM Account
        #                       WHERE Email = %s"""
        # var_tuple = (email)
        # try:
        # cur.execute(signup_query, var_tuple)
        # result = cur.fetchall()
        # except(MySQLdb.Error, MySQLdb.Warning):
        # error = "Email & Password combination does not exist"
        # return_template(login.html, error=error)

        if email in exampleUser and password in exampleUser:
            session['email'] = email
            return redirect(request.args.get("dashboard") or url_for("dashboard"))
        else:
            error = "Email & Password combination does not exist"
            return render_template('one/login.html', error=error)

    return render_template('one/login.html')


@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    if "email" in session:
        email = session['email']
        title = "Welcome " + email
    else:
        return redirect(url_for('index'))
    return render_template('two/dashboard.html', title=title)


@app.route('/logout', methods=["GET"])
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))


@app.route('/profile', methods=["GET", "POST"])
def profile():
    title = "Profile"
    return render_template('two/profile.html', title=title)


@app.route('/matches', methods=["GET", "POST"])
def matches():
    title = "Matches"
    return render_template('two/matches.html', title=title)


@app.route('/messenger', methods=["GET", "POST"])
def messenger():
    title = "Messenger"
    return render_template('two/messenger.html', title=title)


if __name__ == "__main__":
    app.run()
