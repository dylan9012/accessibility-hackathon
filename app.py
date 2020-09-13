from flask import Flask, render_template, request, redirect, session, url_for, flash

app = Flask(__name__)
wsgi_app = app.wsgi_app
app.secret_key = 'e471e07eb0c2977afd4f398907cb78f8'

exampleUser = ["1", "Dylan Barker", "18", "Vision impairment", "E3 3NR", "Disabled", "dylanbarker59@gmail.com", "male",
               "07756756382", "destiny1"]
potential_matches = [["1", "Eyuael Berhe", "Male", "18", "5"],
                     ["2", "Isaac Addo", "Male", "18", "6"],
                     ["3", "Muhriz Tauseef", "Female", "18", "7"]]

likes = [["1", "Eyuael Berhe", "Male", "18", "5"],
         ["2", "Isaac Addo", "Male", "18", "6"],
         ["3", "Muhriz Tauseef", "Female", "18", "7"]]

matched = [["1", "Eyuael Berhe", "Male", "eyuaelberhe@gmail.com", "07765765382"],
           ["2", "Isaac Addo", "Male", "isaacaddo1714@gmail.com", "07962390386"],
           ["3", "Muhriz Tauseef", "Female", "muhriztauseef82@gmail.com", "0794349631"]]


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
                return render_template('one/signup.html', name=name, number=number, email=email, postcode=postcode,
                                       ranges=ranges)

        # Check if email already used

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

        if email in exampleUser and password in exampleUser:  # Replace this with db query
            # Add to user list
            session['id'] = exampleUser[0]
            return redirect(request.args.get("dashboard") or url_for("dashboard"))
        else:
            flash("Email and password combination does not exist", "danger")
            return render_template('one/login.html', email=email)

    return render_template('one/login.html')


@app.route('/logout')
def logout():
    if "id" in session:
        session.pop('id', None)
    return redirect(url_for('index'))


def get_information():
    name = potential_matches[session["page"]][1]
    gender = potential_matches[session["page"]][2]
    age = potential_matches[session["page"]][3]
    distance = potential_matches[session["page"]][4]
    return name, gender, age, distance


@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    if "id" not in session:
        return redirect(url_for('login'))

    if request.method == "POST":
        decision = request.form.get("decision")
        if decision == "Match":
            ...  # Add entry to like table saying interested
        else:
            ...  # Add entry to like table saying not interested

    if "page" in session and request.method == "POST":
        session["page"] += 1
    else:
        session["page"] = 0
    # Run query to get potential matches here and add to potential_matches list
    if len(potential_matches) > session["page"]:
        name, gender, age, distance = get_information()
        return render_template('two/dashboard.html', name=name, gender=gender, age=age, distance=distance)
    else:
        potential_matches.clear()

        session.pop("page", None)
        return render_template('two/dashboard.html', end=True)


@app.route('/requests', methods=["GET", "POST"])
def requests():
    if "id" not in session:
        return redirect(url_for('login'))
    if request.method == "POST":
        selected = None
        for i in range(len(likes)):
            decision_user_id = likes[i][0]
            decision = request.form.get("decision" + decision_user_id)
            if not decision or decision == "Select":
                continue
            else:
                selected = i
        likes.pop(selected) if selected is not None else flash("Choose a decision before pressing submit", "danger")

        # Do query to insert here
    # Query to get their likes
    end = False
    if not likes:
        end = True
    return render_template('two/requests.html', users=likes, end=end)


@app.route('/matches', methods=["GET"])
def matches():
    if "id" not in session:
        return redirect(url_for('login'))
    return render_template('two/matches.html', matches=matched)


@app.route('/profile', methods=["GET"])
def profile():
    if "id" not in session:
        return redirect(url_for('login'))
    # Select query to get details
    name, age, s_d, location, role, email, gender, number, password = exampleUser[1:]
    if role == "Disabled":
        s_d = "Disability: " + s_d
    else:
        s_d = "Speciality: " + s_d

    return render_template('two/profile.html', name=name, age=age, s_d=s_d, location=location, role=role, email=email,
                           gender=gender, number=number, password=password)


if __name__ == "__main__":
    app.run()
