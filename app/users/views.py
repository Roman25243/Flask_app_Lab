from . import user_bp
from flask import render_template, abort, redirect, request, url_for

@user_bp.route('/<string:name>')
def greeting(name):
    name = name.upper()
    age = request.args.get('age', 0, int)
    return render_template('hi.html', name=name, age=age)


@user_bp.route('/admin')
def admin():
    to_url = url_for("users.greeting", age=45, name='administrator', external=True)
    print(to_url)
    return redirect(to_url)