from flask import Flask, render_template, url_for, redirect, request, flash
from forms import ContactForm
from flask_mail import Message, Mail


app = Flask(__name__)
mail = Mail(app)

# Configurations
app.config["SECRET_KEY"] = b"\xf7\xbe\xbc\xad\xfe)*\xe7\xecL\xdf\x15\t\x82\xc7t\x0b\x12;\xf3\xb7J%"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "yourusername@gmail.com"
app.config["MAIL_PASSWORD"] = "your app specific password"

# Routes
@app.route("/")
def view_home():
    return render_template("index.jinja")

@app.route("/about/")
def view_about():
    return render_template("about.jinja")


@app.route("/form", methods=["GET", "POST"])
def contactForm():
	form = ContactForm()
	if request.method == "GET":
		return render_template("contact.jinja", form=form)
	elif request.method == "POST":
		if form.validate() == False:
			flash("All fields are required !")
			return render_template("contact.jinja", form=form)
		else:
			msg = Message(form.subject.data, sender="[SENDER EMAIL]", recipients=["your reciepients gmail id"])
			msg.body = """
			from: %s &lt;%s&gt
			%s
			"""% (form.name.data, form.email.data, form.message.data)
			mail.send(msg)
			return redirect(url_for("index.jinja"))


