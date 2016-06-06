__author__ = 'Bogdan'
__email__ = 'evstrat.bg@gmail.com'
__mobile_phone__ = 89252608400

from flask import Flask, render_template, request
import smtplib


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/gallery.html')
def gallery():
    return render_template('index.html')


@app.route('/contact.html', methods=['GET', 'POST'])
def contacts():
    if request.form:
        email = request.form['email']
        text = request.form['text']
        phone = request.form['phone']
        name = request.form['name']

        # Import smtplib for the actual sending function
        # Open a plain text file for reading.  For this example, assume that
        # the text file contains only ASCII characters.


        # me == the sender's email address
        # you == the recipient's email address

        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP('smtp.gmail.com')
        s.sendmail('evstrat.bg@mail.ru', ['evstrat.bg@gmail.com'], 'qq')
        s.quit()

    return render_template('contact.html')


if __name__ == '__main__':
    app.run()
