from flask import render_template
from karthik_blog_website import app
from karthik_blog_website.models import Post

title = 'flask home page'
@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts = posts, title='title')


@app.route("/about")
def about():
    return render_template('about.html', title='about')