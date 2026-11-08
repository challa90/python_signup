from flask import Flask, render_template, request, redirect, url_for
import os
import psycopg2

app = Flask(__name__)

# PostgreSQL Connection
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return conn

@app.route('/')
def home():
    return redirect(url_for('signup'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO users (username, email, password)
            VALUES (%s, %s, %s)
            """,
            (username, email, password)
        )

        conn.commit()
        cur.close()
        conn.close()

        return "Signup Successful!"

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
