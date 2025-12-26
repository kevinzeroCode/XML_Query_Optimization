from flask_wtf import FlaskForm
from wtforms import SubmitField


class XMLEditForm(FlaskForm):
    download = SubmitField('Сваляне')
