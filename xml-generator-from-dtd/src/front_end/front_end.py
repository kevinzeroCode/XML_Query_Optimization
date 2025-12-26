"""
The main module - starts the application,
handles the connection between pages and contains some of the logic
"""
from flask import Flask, render_template
from config import Config
from src.dtd_parser.dtd_parser import DTDParser
from src.wiki_api.wiki_api import WikiAPI, Content, RequestType
from src.xml_generator.xml_generator import XMLGenerator
from src.xml_document.xml_document import XMLDocument, IncompatibleException
from src.consts import HEADER_TEXT_REQUEST_LITERAL, HEADER_IMAGE_REQUEST_LITERAL, \
    HEADER_TEXT_IMAGE_REQUEST_LITERAL, TEXT_LITERAL, IMAGE_LITERAL, NO_WIKI
from .file_upload_form import FileUploadForm

APP = Flask(__name__)
APP.config.from_object(Config)


def get_content(title: str, request: RequestType) -> Content:
    """
    Gets the content of a Wikipedia article
    :param title: The title of the searched article
    :param request: The type of the request
    :return: Content object containing the wikipedia article
    """
    wiki_getter = WikiAPI()

    if request == RequestType.HEADER_TEXT:
        return wiki_getter.get_page_header_text(title)
    elif request == RequestType.HEADER_IMAGE:
        return wiki_getter.get_page_header_image(title)
    elif request == RequestType.HEADER_TEXT_IMAGE:
        return wiki_getter.get_page_header_text_image(title)
    elif request == RequestType.TEXT:
        return wiki_getter.get_page_text(title)
    elif request == RequestType.IMAGE:
        return wiki_getter.get_page_images(title)
    else:
        raise ValueError("Invalid request type. Valid RequestType is: HEADER_TEXT, HEADER_IMAGE, "
                         "HEADER_TEXT_IMAGE, TEXT or IMAGE")


def __convert_request_literal_to_enum(request_literal: str) -> RequestType:
    if request_literal == HEADER_TEXT_REQUEST_LITERAL:
        return RequestType.HEADER_TEXT
    elif request_literal == HEADER_IMAGE_REQUEST_LITERAL:
        return RequestType.HEADER_IMAGE
    elif request_literal == HEADER_TEXT_IMAGE_REQUEST_LITERAL:
        return RequestType.HEADER_TEXT_IMAGE
    elif request_literal == TEXT_LITERAL:
        return RequestType.TEXT
    elif request_literal == IMAGE_LITERAL:
        return RequestType.IMAGE
    elif request_literal == NO_WIKI:
        return RequestType.NONE
    else:
        raise ValueError("Invalid request type. Valid RequestType is: HEADER_TEXT, HEADER_IMAGE, "
                         "HEADER_TEXT_IMAGE, TEXT or IMAGE")


@APP.route('/', methods=['GET', 'POST'])
@APP.route('/index', methods=['GET', 'POST'])
def index():
    """
    Loads the main page
    :return:
    """
    file_upload_form = FileUploadForm()
    if file_upload_form.validate_on_submit():
        file_handle = file_upload_form.dtd.data
        dtd_string = file_handle.read()

        request_type = __convert_request_literal_to_enum(file_upload_form.request_type.data)
        if file_upload_form.wiki_article_name.data == '' and request_type is not RequestType.NONE:
            return 'Не е възможно да се направи заявка за wikipedia без име на статия'

        parser = DTDParser()
        parser.parse_string(dtd_string.decode('utf-8'))
        xml_generate = XMLGenerator(parser)

        xml_document: XMLDocument = xml_generate.generate_xml()
        if request_type is not RequestType.NONE:
            try:
                wiki_content = get_content(file_upload_form.wiki_article_name.data, request_type)
            except KeyError:
                return 'Не съществува такава страница в Wikipedia'

        try:
            if request_type is not RequestType.NONE:
                xml_document.fill_content(wiki_content)
        except IncompatibleException:
            return 'Това DTD не отговаря на Wikipedia статия'

        return render_template('xml_edit.html', project_name='Генериране на XML по DTD и статия в Wikipedia',
                               xml_to_edit=xml_document.to_string())

    return render_template('index.html', project_name='Генериране на XML по DTD и статия в Wikipedia',
                           form=file_upload_form)
