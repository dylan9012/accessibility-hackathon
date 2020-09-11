from flask import Flask, render_template, request, redirect, session, url_for, flash

# import MySQLdb

app = Flask(__name__)
wsgi_app = app.wsgi_app
app.secret_key = 'e471e07eb0c2977afd4f398907cb78f8'

exampleUser = ["1", "Dylan Barker", "18", "Vision impairment", "E3 3NR", "Disabled", "dylanbarker59@gmail.com", "male",
               "07756756382", "destiny1"]
matches = ["", "Marcus Biller", "Breann Delee", "Chu Bertolini", "Eliseo Spell", "Onita Coffin", "Maribeth Langlais",
           "Sharyn Turck", "Gil Silvia", "Brande Paiva", "Sierra Horney", "Antony Melcher", "Mia Dill",
           "Leora Deherrera", "Aleida Ghee", "Ervin Phou", "Missy Vandergrift", "Dawne Freshwater", "Lyle Arends",
           "Ora Kimberling", "Carolee Saini", "Leontine Luczak", "Tijuana Aubuchon", "Maryland Hutchinson",
           "Emanuel Kari", "Ria Wimbish", "Wanetta Rountree", "Cassy Claborn", "Adah Moncrief", "Victoria Rustin",
           "Renita Tuft", "Newton Hamlet", "Aletha Sturgeon", "Jeraldine Eisenberg", "Alvin Jeffreys", "Brady Toth",
           "Georgann Curfman"]
non_matches = ["Stacia Lucas", "Heike Thrash", "Sari Kirkbride", "Risa Welke", "Leonore Loveall", "Alina Letchworth",
               "Viva Hammaker", "Cinda Rhoads", "Arielle Awong", "Kirk Swingle", "Dina Moeckel", "Freida Latimore",
               "Georgina Schertz", "Merlyn Childers", "Katharina Pough", "Samella Wymer", "Dixie Weyand", "Tomi Eden",
               "Fernando Schapiro", "Terrie Logston", "Damon Zirkle", "Travis Schreck", "Juan Sears", "Lon Glennon",
               "Graham Groleau", "Barrie Manson", "Percy Garner", "Porsche Uribe", "Jami Fujimoto", "Mitchel Rioux",
               "Kathe Galvan", "Mariella Lundquist", "Justa Mumma", "Gabriella Mclennon", "Liza Corlett",
               "Reed Stapler", "Ione Merlo", "Hermelinda Crass", "Elfrieda Place", "Glady Ferri", "Madie Binkley",
               "Beatriz Fritch", "Salvador Kenton", "Freddie Jovel", "Lyle Saleh"]


# def create_connection():
#   return MySQLdb.connect(
#               host='dylan9012.mysql.pythonanywhere-services.com',
#               user='dylan9012',
#               password='destiny1',
#               db='dylan9012$default',
#               cursorclass=MySQLdb.cursors.Dictcursor
#   )


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
                flash("Please fill in all fields", "danger")
                return render_template('one/signup.html', name=name, user_age=age, number=number, s_d=s_d, gender=gender
                                       , email=email, postcode=postcode, role=role)

        # - Check if email already used

        # with connection().cursor as cur:
        # signup_query = """INSERT INTO Account (Name, Age, Needs_or_Specialty, Location, Carer_or_client, Email,
        # Gender, Phone_number, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        # var_tuple = (name, age, s_d, postcode, role, email, gender, number, password)
        # cur.execute(signup_query, var_tuple)
        # cur.commit()

        flash("Sign up has succeeded, please login", "success")
        return redirect(url_for('login'))
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
                flash("Please fill in all fields", "danger")
                return render_template('one/login.html', email=email)

        # with connection().cursor as cur:
        #   login_query = """SELECT Password, Email FROM Account WHERE Email = %s"""
        #   try:
        #       cur.execute(signup_query, email)
        #       result = cur.fetchall()
        #   except(MySQLdb.Error, MySQLdb.Warning):
        #       error = "Email & Password combination does not exist"

        if email in exampleUser and password in exampleUser:
            session['email'] = email
            return redirect(request.args.get("dashboard") or url_for("dashboard"))
        else:
            flash("Email and password combination does not exist", "danger")
            return render_template('one/login.html', email=email)

    return render_template('one/login.html')


@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    if "email" in session:
        email = session['email']
        name = email[:5].title()  # - For exampleUser specifically
    else:
        return redirect(url_for('login'))
    return render_template('two/dashboard.html', name=name)


@app.route('/logout')
def logout():
    if "email" in session:
        session.pop('email', None)
    return redirect(url_for('index'))


@app.route('/profile', methods=["GET", "POST"])
def profile():
    if "email" not in session:
        return redirect(url_for('login'))
    return render_template('two/profile.html')


@app.route('/matches', methods=["GET", "POST"])
def matches():
    if "email" not in session:
        return redirect(url_for('login'))
    return render_template('two/matches.html')


@app.route('/grant', methods=["GET"])
def grant():
    if "email" not in session:
        return redirect(url_for('login'))
    return render_template('two/grant.html')


if __name__ == "__main__":
    app.run()
