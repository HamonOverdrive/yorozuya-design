from flask import Flask, render_template, request, flash, redirect
from flask_mail import Mail, Message
from wtforms import Form, StringField, SubmitField, validators, SelectField, TextAreaField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'exampleemail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


class MessageForm(Form):
    name = StringField('Name', [validators.Length(min=1)])
    email = StringField('Email Address', [validators.Length(min=6, max=25)])
    dropdown = SelectField(u'Project', choices=[('c1', 'Project'), ('c2', 'Web'), ('c3', 'Data Analysis'), ('c4', 'Brands'), ('c5', 'Other')])
    text = TextAreaField('Message Us', [validators.Length(min=1, max=300)])
    submit = SubmitField('Send Message')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MessageForm(request.form)
    # if post form information gets sent to email with information
    if request.method == 'POST' and form.validate():
        msg = Message(subject=request.form.get('dropdown'), sender=request.form.get('email'), recipients=['robinleesuns13@gmail.com'])
        msg.body = request.form.get('text')
        mail.send(msg)
        return redirect('index')
    return render_template("index.html", form=form)


if __name__ == '__main__':
    app.run()
