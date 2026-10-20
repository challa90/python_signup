from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# PostgreSQL Connection
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="flaskdb",
        user="postgres",
        password="Postgres"
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
    app.run(debug=True)
