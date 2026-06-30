from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/birthday")
def birthday():
     person = {
        "name": "Cupcake",
        "message": "Write your message here"
     }
     wishes = [
        "May all your dreams come true 🌟",
        "Wishing you endless happiness 💕",
        "You deserve all the good things 🎂(me 😏)"
     ]
     return render_template("birthday.html", person=person,wishes=wishes)

if __name__ == "__main__":
    app.run(debug=True)