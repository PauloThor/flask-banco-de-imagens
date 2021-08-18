from flask.testing import FlaskClient

def test_files_status_code(client: FlaskClient):
    response = client.get("/files")

    assert (
        response.status_code == 200
    ), 'Status incorreto'


def test_files_json_response(client: FlaskClient):
    response = client.get('/files')
    
    assert type(response.get_json()) == list, "Não retornou uma lista"
