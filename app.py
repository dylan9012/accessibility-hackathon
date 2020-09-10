from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
wsgi_app = app.wsgi_app
app.secret_key = 'somesecretkey'


@app.route('/')
def index():
    title = "Home"
    return render_template('index.html', title=title)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    team = ["Dylan Barker: dylanbarker59@gmail.com | King's College London ",
            "Eyuael Berhe: eyuael.berhe@gmail.com | Warwick University",
            "Isaac Addo: isaacaddo1714@gmail.com | King's College London",
            "Muhriz Tauseef: muhriztauseef82@gmail.com | King's College London"]
    return render_template('contact.html', team=team)


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
        image = request.files["image"]
        entries.extend((name, age, number, gender, email, password, postcode, role, s_d, image))
        for i in entries:
            if not i:
                error = "Please fill in all fields"
                return render_template('signup.html', error=error, name=name, user_age=age, number=number, s_d=s_d,
                                       gender=gender, email=email, password=password, postcode=postcode, role=role,
                                       image=image)
        success = "Sign up has succeeded, please login"
        return render_template('login.html', success=success)
    return render_template('signup.html')


@app.route('/login')
def login():
    return render_template('login.html')
