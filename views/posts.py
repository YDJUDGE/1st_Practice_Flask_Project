from flask import (
    Blueprint,
    jsonify,
    render_template,
    request,
    url_for,
    redirect,
    flash

)

from sqlalchemy.exc import IntegrityError, DatabaseError

from models import db

from werkzeug.exceptions import BadRequest, InternalServerError

from views.forms.posts import AddPostForm

from models import Post, ViewCount, Comment

post_app = Blueprint("post_app", __name__)

@post_app.get("/", endpoint="list")
def index():
    posts = Post.query.order_by(Post.id).all()
    return render_template("blog/index.html", posts=posts)


@post_app.get("/<int:post_id>/", endpoint="detail")
def detail(post_id: int):
    post = Post.query.get_or_404(post_id, f"Post #{post_id} not found")

    v = post.c

    if v is None:
        v = ViewCount(view_count=post.id, count=0)
        db.session.add(v)
        db.session.commit()

    v.plus_count()

    return render_template("blog/detail.html", post=post, views=v.count)


@post_app.route("/<int:post_id>/delete/", methods=["GET", "POST"], endpoint="delete")
def delete_post(post_id: int):
    post = Post.query.get_or_404(post_id, f"Post #{post_id} not found!")
    if request.method == "GET":
        return render_template("blog/delete-post.html", post=post)
    post_name = post.title
    db.session.delete(post)
    try:
        db.session.commit()
    except Exception as e:
        print(e)

    flash(f"Deleted post - {post_name}", "warning")
    url = url_for("post_app.list")
    return redirect(url)


@post_app.route("/add", methods=["GET", "POST"], endpoint="add")
def add_post():
    form = AddPostForm()
    if request.method == "GET":
        return render_template("blog/add.html", form=form)
    if not form.validate_on_submit():
        return render_template("blog/add.html", form=form), 400

    title_name = form.title.data
    description_name = form.description.data
    post = Post(title=title_name, description=description_name)
    db.session.add(post)
    try:
        db.session.commit()
    except IntegrityError:
        raise BadRequest(f"Could not save post, probably the {title_name} not valid!")
    except DatabaseError:
        raise InternalServerError("could not save post due to an internal error")

    flash(f"Successful add new post - {title_name}!")
    url = url_for("post_app.detail", post_id=post.id)
    return redirect(url)

@post_app.route('/post/<int:post_id>/add_comment', methods=["POST"])
def add_comment(post_id: int):
    post = Post.query.get_or_404(post_id)
    comment_body = request.form.get('comment_body')

    if comment_body:
        comment = Comment(body=comment_body, post_id=post.id)
        db.session.add(comment)
        db.session.commit()

    return redirect(url_for('post_app.detail', post_id=post.id))
