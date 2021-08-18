from flask.testing import FlaskClient
from flask import request

def test_download_zip_method_is_only_get(client: FlaskClient):

    assert 'POST' not in (client.options('/download-zip?file_type=jpg&compression_rate=5').headers['Allow'])


def test_download_zip_params(client: FlaskClient):
    _ = client.get('/download-zip?file_type=jpg&compression_rate=5')

    assert request.args['file_type'] == 'jpg'
    assert request.args['compression_rate'] == '5'
