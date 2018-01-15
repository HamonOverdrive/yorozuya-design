from flask import Flask, render_template
from flask_mail import Mail


app = Flask(__name__)
mail = Mail(app)


@app.route('/')
def index():
	return render_template("index.html")


if __name__ == '__main__':
	app.run()
