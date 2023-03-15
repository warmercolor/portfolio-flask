from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.getenv("EMAIL")
app.config["MAIL_PASSWORD"] = os.getenv("PASSWORD")

mail = Mail(app)


class Contact:
    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        form_contact = Contact(
            request.form["name"], request.form["email"], request.form["message"]
        )
        msg = Message(
            subject=f"{form_contact.name} te enviou uma mensagem no portfólio",
            sender=form_contact.email,
            recipients=["thaisalic3@gmail.com"],
            body=f"""

                {form_contact.name} com o e-mail {form_contact.email}, te enviou a seguinte mensagem:

                {form_contact.message}

            """,
        )

        mail.send(msg)
        flash("Mensagem enviada com sucesso!")
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
