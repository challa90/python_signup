from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage
users = []

@app.route("/")
def home():
    return redirect(url_for("signup"))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    message = ""

    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        users.append({
            "username": username,
            "email": email,
            "password": password
        })

        message = "Signup successful!"

    return render_template("signup.html", message=message)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
