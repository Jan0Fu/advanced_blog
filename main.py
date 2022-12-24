from flask import Flask, render_template
import requests


posts = requests.get("https://api.npoint.io/2614b7cf1520299f67ca").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template('index.html', posts=posts)


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
