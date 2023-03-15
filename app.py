from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from config import key, email, password

app = Flask(__name__)
mail = Mail(app)
app.secret_key = key

mail_settings = {
    "MAIL_SERVER": "smtp.gmail.com",
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": password,
}

app.config.update(mail_settings)


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
        message = Message(
            subject=f"{form_contact.name} te enviou uma mensagem no portfólio",
            sender=app.config.get("MAIL_USERNAME"),
            recipients=["thaisalic3@gmail.com", app.config.get("MAIL_USERNAME")],
            body=f"""

                {form_contact.name} com o e-mail {form_contact.email}, te enviou a seguinte mensagem:

                {form_contact.message}

            """,
        )

        mail.send(message)
        flash("Mensagem enviada com sucesso!")
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
