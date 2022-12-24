from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template('index.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
