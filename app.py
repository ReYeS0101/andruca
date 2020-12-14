from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'dev'

if ENV == 'prod':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Kaled.2021@localhost/Andruca'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yshdmhratwnolz:ddb4f05d09a29b1f99bb551a8d4ea25938177707a0452de7d3b886fa18bc576b@ec2-3-215-83-17.compute-1.amazonaws.com:5432/d8p0png9t0bsrf'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Vendido(db.Model):
    __tablename__ = 'vendido'
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(200), unique=True)
    producto = db.Column(db.String(200))
    comments = db.Column(db.Text())

    def __init__(self, cliente, producto, comments):
        self.cliente = cliente
        self.producto = producto
        self.comments = comments


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        cliente = request.form['cliente']
        producto = request.form['producto']
        comments = request.form['comments']
        # print(customer, dealer, rating, comments)
        if cliente == '' or producto == '':
            return render_template('contacto.html', message='Por favor complete los datos')
        if db.session.query(Vendido).filter(Vendido.cliente == cliente).count() == 0:
            data = Vendido(cliente, producto, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(cliente, producto, comments)
            return render_template('contacto.html')
        return render_template('contacto.html', message='Recibimos su Mensaje')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


@app.route('/promo')
def promo():
    return render_template('promo.html')


@app.route('/organizador')
def organizador():
    return render_template('organizador.html')


@app.route('/matero')
def matero():
    return render_template('matero.html')


@app.route('/almohadon')
def almohadon():
    return render_template('almohadon.html')


@app.route('/info')
def info():
    return render_template('info.html')


if __name__ == '__main__':
    app.run()
