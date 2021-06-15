from flask import *

# create an instance of flask
app = Flask(__name__)


# create a route
@app.route('/')
def index():
    research_links = ['Research gate', 'MDPI', 'Wiley', 'Taylor and Francis']
    return render_template('index.html', names = research_links)


@app.route('/login')
def login():

    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/registrant', methods = ['POST'])
def registrant():

    firstname = request.form.get('first_name')
    lastname = request.form.get('last_name')
    other_name = request.form.get('other_name')
    level = request.form.get('level')
    phone = request.form.get('phone_number')
    email = request.form.get('email')
    date_of_birth = request.form.get('birthday')

    if not other_name:
        other_name = ""

    fullname = firstname + " " + lastname + " " + other_name

    return render_template('registrant.html', fullname = fullname, level=level, phone=phone, email=email, date_of_birth=date_of_birth)


if __name__ == '__main__':
    app.run(debug = True)