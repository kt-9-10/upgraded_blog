from flask import Flask, render_template
import requests


request = requests.get('https://api.npoint.io/97fc305e1725631f01e1')
all_posts = request.json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<post_id>")
def get_post(post_id):
    requested_post = None
    for post in all_posts:
        if int(post_id) == post['id']:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
