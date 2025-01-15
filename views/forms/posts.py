from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length

class AddPostForm(FlaskForm):
    title = StringField("Заголовок", name="post-name", validators=[DataRequired(), Length(2)])
    description = StringField("Описание", name="desc-name", validators=[DataRequired(), Length(5)])

