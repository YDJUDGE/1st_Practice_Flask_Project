from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length

class AddUserForm(FlaskForm):
    username = StringField("Никнейм", name="username-user", validators=[DataRequired(), Length(5)])
    is_author = BooleanField("Хотите быть автором?", default=False)

