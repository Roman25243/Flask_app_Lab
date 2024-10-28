from flask import  request, url_for, redirect, render_template, abort
from app import app
@app.route('/')
def main():
    return render_template ("base.html")

@app.route('/homepage') 
def home():
    """View for the Home page of your website."""
    agent = request.user_agent
    return render_template ("home.html", agent=agent )


@app.route('/hi/<string:name>')
def greeting(name):
    name = name.upper()
    age = request.args.get('age', None, int)
    
    
    return render_template ("hi.html", name=name, age=age )


posts = [
    {"id": 1, 'title': 'My First Post',
        'content': 'This is the content of my first post.', 'author': 'John Doe'},
    {"id": 2, 'title': 'Another Day',
        'content': 'Today I learned about Flask macros.', 'author': 'Jane Smith'},
    {"id": 3, 'title': 'Flask and Jinja2',
        'content': 'Jinja2 is powerful for templating.', 'author': 'Mike Lee'}
]

@app.route('/posts')
def get_posts():
    return render_template("posts.html", posts=posts)

@app.route('/admin')
def admin():
    to_url = url_for("greeting", name='administrator', age=45, _external=True)
    print(to_url)
    return redirect(to_url)

@app.route('/post/<int:id>')
def get_post(id):
    if id > len(posts):
        abort(404)
    post = posts[id-1]
    return render_template('detail-post.html', post=post)

@app.route('/resume')
def resume():
    return render_template('resume.html', title='Моє резюме')