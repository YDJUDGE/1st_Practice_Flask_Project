from flask import Flask, render_template
from flask_migrate import Migrate
from models.database import db
from config import SECRET_KEY, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATION
from views.posts import post_app
from views.users import user_app

app = Flask(__name__)

app.config.update(
    SECRET_KEY=SECRET_KEY,
    SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATION=SQLALCHEMY_TRACK_MODIFICATION)

db.init_app(app)
db.app = app

migrate = Migrate(app, db, compare_type=True)

app.register_blueprint(post_app, url_prefix="/posts")
app.register_blueprint(user_app, url_prefix="/users")


@app.get("/", endpoint="home")
def home_page():
    return render_template("index.html")


