from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired
from wtforms import SubmitField, StringField, RadioField
from src.consts import IMAGE_LITERAL, TEXT_LITERAL, HEADER_TEXT_IMAGE_REQUEST_LITERAL,\
    HEADER_IMAGE_REQUEST_LITERAL, HEADER_TEXT_REQUEST_LITERAL, NO_WIKI


class FileUploadForm(FlaskForm):
    """
    The file upload form, which is used to get the DTD file, the wiki article and the request type
    """
    dtd = FileField(validators=[FileRequired()])
    wiki_article_name = StringField('Name')
    request_type = RadioField('Изберете каква информация да се вземе',
                              choices=[(HEADER_TEXT_REQUEST_LITERAL,
                                        'Вземи заглавията на секциите и текста'),
                                       (HEADER_IMAGE_REQUEST_LITERAL,
                                        'Вземи заглавията на секциите и изображенията'),
                                       (HEADER_TEXT_IMAGE_REQUEST_LITERAL,
                                        'Вземи заглавията на секциите, текста и изображенията'),
                                       (TEXT_LITERAL, 'Вземи само текста'),
                                       (IMAGE_LITERAL, 'Вземи само изображенията'),
                                       (NO_WIKI, 'Не използвай Wikipedia')],
                              default=1)
    submit = SubmitField('Генериране')
