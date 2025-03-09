from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from .models import Post
from .models import User
from . import db

views=Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
@login_required     #Restricting Page accesss
def home():
    allposts=Post.query.all()
    return render_template("home.html", title="HomePage", user=current_user, posts=allposts)

@views.route("/create-post", methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method=="POST":
        text=request.form.get("text")
        if len(text)<1:
            flash("Post is too short", category="error")
        else:
            new_post=Post(text=text, author=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            flash("Post created", category="success")
            return redirect(url_for('views.home'))
    return render_template("create_post.html", title="Create Post", user=current_user)

@views.route("/delete-post/<int:id>")
def delete_post(id):
    post=Post.query.filter_by(id=id).first()
    if not post:
        flash("Post does not exist", category="error")
    elif current_user.id!=post.author:
        flash("You don't have permission to delete this post", category="error")
    else:
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted", category="success")
    return redirect(url_for('views.home'))

@views.route("/posts/<username>")
@login_required
def posts(username):
    user=User.query.filter_by(username=username).first()
    
    
    if not user:
        flash("User does not exist", category="error")
        return redirect(url_for('views.home'))
    
    # posts=Post.query.filter_by(author=user.id).all()
    posts=user.posts
    return render_template("posts.html", title=username, user=current_user, posts=posts)
