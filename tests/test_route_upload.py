from flask.testing import FlaskClient
from werkzeug.datastructures import FileStorage
import os

files_path = os.environ.get('FILES_DIRECTORY')


def test_upload_status_code_201(client: FlaskClient):
    
    with open('./teste.png', 'rb') as image:
        my_file = FileStorage(stream=image, filename='teste.png', content_type='image/png')

        response = client.post('/upload', data={'file': my_file}, content_type='multipart/form-data')
        assert (
            response.status_code == 201
        ), "Status incorreto"

        os.remove(f'./files/png/teste.png')


def test_upload_error_409_if_file_exists(client: FlaskClient):
    
    with open('./teste.png', 'rb') as image:
        my_file = FileStorage(stream=image, filename='kenzie.png', content_type='image/png')

        response = client.post('/upload', data={'file': my_file}, content_type='multipart/form-data')
        assert (
            response.status_code == 409
        ), "Status incorreto"