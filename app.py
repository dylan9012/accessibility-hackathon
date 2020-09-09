from flask import Flask, render_template

app = Flask(__name__)


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


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
