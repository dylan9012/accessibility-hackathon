from flask import Flask, render_template, request, redirect, session, url_for, flash

from tools.GetRequests import GetRequest
from tools.Likes import FindLikes
from tools.Matches import FindMatches
from tools.UserInfo import GetInfo
from tools.login_query import ValidateLogIn
from tools.register_query import ValidateSignUp

app = Flask(__name__)
wsgi_app = app.wsgi_app
app.secret_key = 'e471e07eb0c2977afd4f398907cb78f8'

logged_user = []
potential_matches = []

likes = []

matched = []


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

        if not ValidateSignUp(email, name, age, s_d, ranges, postcode, role, gender, number, password).sign_up():
            flash("Email has already been used, try another")
            return redirect(url_for('signup'))

        flash("Sign up has succeeded, please login", "success")
        return redirect(url_for('login'))
    return render_template('one/signup.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    global logged_user
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        for i in (email, password):
            if not i:
                flash("Please fill in all fields", "danger")
                return render_template('one/login.html', email=email)

        identity = ValidateLogIn(email, password).log_in()
        if identity:
            logged_user = GetInfo(identity).Info()
            session['id'] = logged_user[0]
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
    return potential_matches[session["page"]][1:]


@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    global potential_matches
    if "id" not in session:
        return redirect(url_for('login'))

    if request.method == "POST":
        decision = request.form.get("decision")
        if decision == "Match":
            FindLikes(session['id'])
        else:
            ...  # Add entry to like table saying not interested

    if "page" in session and request.method == "POST":
        session["page"] += 1
    else:
        session["page"] = 0

    potential_matches = FindMatches(session["id"]).PotentialMatches()
    if len(potential_matches) > session["page"]:
        name, gender, age, distance = get_information()
        return render_template('two/dashboard.html', name=name, gender=gender, age=age, distance=distance)
    else:
        potential_matches.clear()
        # ----------------------------------------------------------------------
        session.pop("page", None)
        return render_template('two/dashboard.html', end=True)


@app.route('/requests', methods=["GET", "POST"])
def requests():
    global likes
    if "id" not in session:
        return redirect(url_for('login'))

    likes = GetRequest(session['id']).FindRequests()

    if request.method == "POST":
        selected = None
        for i in range(len(likes)):
            decision_user_id = likes[i][0]
            decision = request.form.get("decision" + decision_user_id)
            if not decision or decision == "Select":
                continue
            else:
                selected = i
        if selected is not None:
            likes.pop(selected)
            a = FindLikes(session['id'], likes[selected][0]).Like()
        else:
            flash("Choose a decision before pressing submit", "danger")

        # Do query to insert here

    end = False
    if not likes:
        end = True
    return render_template('two/requests.html', users=likes, end=end)


@app.route('/matches', methods=["GET"])
def matches():
    global matched
    if "id" not in session:
        return redirect(url_for('login'))
    return render_template('two/matches.html', matches=matched)


@app.route('/profile', methods=["GET"])
def profile():
    global logged_user
    if "id" not in session:
        return redirect(url_for('login'))

    name, age, s_d, location, role, email, gender, number, password = logged_user[1:]
    if role == "Disabled":
        s_d = "Disability: " + s_d
    else:
        s_d = "Speciality: " + s_d

    return render_template('two/profile.html', name=name, age=age, s_d=s_d, location=location, role=role, email=email,
                           gender=gender, number=number, password=password)


if __name__ == "__main__":
    app.run()
