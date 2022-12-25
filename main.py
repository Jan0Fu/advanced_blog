from flask import Flask, render_template, request
import smtplib
import requests

email = ""
password = ""

posts = requests.get("https://api.npoint.io/2614b7cf1520299f67ca").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template('index.html', posts=posts)


@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template('contact.html', msg_sent=True)
    return render_template('contact.html', msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(from_addr=email, to_addrs=email, email_message)


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
