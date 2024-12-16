import json
import os
from . import post_bp
from flask import render_template, abort, flash, redirect, url_for, current_app
from .forms import PostForm
from datetime import datetime

@post_bp.route('/add_post', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        json_path = os.path.join(current_app.root_path, 'posts.json')
        
        posts = []
        if os.path.exists(json_path):
            with open(json_path, 'r') as f:
                posts = json.load(f)
        
        new_post = {
            "id": len(posts) + 1,
            "title": form.title.data,
            "content": form.content.data,
            "category": form.category.data,
            "is_active": form.is_active.data,
            "publication_date": form.publish_date.data.strftime('%Y-%m-%d'),
            "author": "Current User"  
        }
        
        posts.append(new_post)
        
        with open(json_path, 'w') as f:
            json.dump(posts, f, indent=4)
        
        flash(f'Post "{form.title.data}" added successfully!', 'success')
        return redirect(url_for('.get_posts'))
    
    return render_template("add_post.html", form=form)

@post_bp.route('/')
def get_posts():
    json_path = os.path.join(current_app.root_path, 'posts.json')
    posts = []
    if os.path.exists(json_path):
        with open(json_path, 'r') as f:
            posts = json.load(f)
    return render_template("posts.html", posts=posts)

@post_bp.route('/<int:id>')
def detail_post(id):
    json_path = os.path.join(current_app.root_path, 'posts.json')
    if os.path.exists(json_path):
        with open(json_path, 'r') as f:
            posts = json.load(f)
        
        post = next((p for p in posts if p['id'] == id), None)
        if post:
            return render_template("detail-post.html", post=post)
    
    abort(404)