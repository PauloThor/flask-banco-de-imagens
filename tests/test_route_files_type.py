from flask.testing import FlaskClient


def test_files__by_type_status_code(client: FlaskClient):
    response = client.get("/files/png")
    
    assert (
        response.status_code == 200
    ), 'Status incorreto'


def test_files__by_type_json_response(client: FlaskClient):
    response = client.get('/files/png')
    
    assert type(response.get_json()) == list, "Não retornou uma lista"
