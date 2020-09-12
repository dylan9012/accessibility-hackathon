from flask import Flask, render_template, request, redirect, session, url_for, flash

# import MySQLdb

app = Flask(__name__)
wsgi_app = app.wsgi_app
app.secret_key = 'e471e07eb0c2977afd4f398907cb78f8'

exampleUser = ["1", "Dylan Barker", "18", "Vision impairment", "E3 3NR", "Disabled", "dylanbarker59@gmail.com", "male",
               "07756756382", "destiny1"]
potential_matches = [["Eyuael Berhe", "Male", "18", "Vision impairment", "5"],
                     ["Isaac Addo", "Male", "18", "Deaf or hard of hearing", "6"],
                     ["Muhriz Tauseef", "Male", "18", "Autism Spectrum Disorder", "7"]]


@app.route('/')
def index():
    if "id" in session:
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
        name = request.form.get("name")
        age = request.form.get("age")
        number = request.form.get("number")
        gender = request.form.get("gender")
        email = request.form.get("email")
        password = request.form.get("password")
        postcode = request.form.get("postcode")
        role = "true" if request.form.get("role") == "carer" else "false"
        s_d = request.form.get("speciality_or_disabled")
        ranges = request.form.get("range")
        for i in (name, age, number, gender, email, password, postcode, role, s_d, ranges):
            if not i or i == "Select":
                flash("Please fill in all fields", "danger")
                return render_template('one/signup.html', name=name, user_age=age, number=number, s_d=s_d,
                                       gender=gender, email=email, postcode=postcode, role=role, ranges=ranges)

        # - Check if email already used

        flash("Sign up has succeeded, please login", "success")
        return redirect(url_for('login'))
    return render_template('one/signup.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        for i in (email, password):
            if not i:
                flash("Please fill in all fields", "danger")
                return render_template('one/login.html', email=email)

        if email in exampleUser and password in exampleUser:  # - Replace this with db query
            session['id'] = exampleUser[0]
            return redirect(request.args.get("dashboard") or url_for("dashboard"))
        else:
            flash("Email and password combination does not exist", "danger")
            return render_template('one/login.html', email=email)

    return render_template('one/login.html')


@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    if "id" in session:
        if "d-page" in session:
            session["d-page"] += 1
            name = potential_matches[session["d-page"]][0]
            gender = potential_matches[session["d-page"]][1]
            age = potential_matches[session["d-page"]][2]
            s_d = potential_matches[session["d-page"]][3]
            distance = potential_matches[session["d-page"]][4]
            

        else:
            ...
    else:
        return redirect(url_for('login'))
    return render_template('two/dashboard.html', name=exampleUser[1])


@app.route('/logout')
def logout():
    if "id" in session:
        session.pop('id', None)
    return redirect(url_for('index'))


@app.route('/matches', methods=["GET", "POST"])
def matches():
    if "id" not in session:
        return redirect(url_for('login'))
    return render_template('two/matches.html')


@app.route('/profile', methods=["GET"])
def profile():
    if "id" not in session:
        return redirect(url_for('login'))
    return render_template('two/profile.html')


if __name__ == "__main__":
    app.run()
