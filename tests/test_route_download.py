from flask.testing import FlaskClient
from werkzeug.datastructures import FileStorage
import os

files_path = os.environ.get('FILES_DIRECTORY')


def test_download_status_code_200(client: FlaskClient):
    response = client.get('/download/kenzie.png')

    assert (response.status_code == 200), response


def test_download_status_code_404_if_file_doenst_exist(client: FlaskClient):
    response = client.get('/download/kenzieee.png')

    assert (response.status_code == 404), response
