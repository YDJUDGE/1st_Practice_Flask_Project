from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
    flash

)

from sqlalchemy.exc import IntegrityError, DatabaseError

from models import db

from werkzeug.exceptions import BadRequest, InternalServerError

from views.forms.users import AddUserForm

from models import User

user_app = Blueprint("user_app", __name__)

@user_app.route("/add_user", methods=["GET", "POST"], endpoint="add_user")
def add_user():
    form = AddUserForm()
    if request.method == "GET":
        return render_template("blog/add_user.html", form=form)
    if not form.validate_on_submit():
        return render_template("blog/add_user.html", form=form), 400

    username = form.username.data
    is_author = form.is_author.data
    user = User(username=username, is_author=is_author)
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError:
        raise BadRequest(f"Could not save your account {username} is not valid!")
    except DatabaseError:
        raise InternalServerError("could not save product due to an internal error")

    flash(f"Successful add - {username}!")
    url = url_for("user_app.add_user")
    return redirect(url)
