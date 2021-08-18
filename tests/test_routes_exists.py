from pytest import fail
from werkzeug.exceptions import NotFound
from werkzeug.exceptions import InternalServerError


def test_route_files_exists(route_matcher):
    try:
        assert route_matcher("/files")
    except NotFound:
        fail('Verifique se a rota "/files" existe')
    except InternalServerError:
        fail(
            'Seu servidor está com erro interno na rota "/files", essa rota não é capaz de processar uma requisição'
        )


def test_route_files_type_exists(route_matcher):
    try:
        assert route_matcher("/files/png")
    except NotFound:
        fail('Verifique se a rota "/files/<file_type>" existe')
    except InternalServerError:
        fail(
            'Seu servidor está com erro interno na rota "/files", essa rota não é capaz de processar uma requisição'
        )


def test_route_download_exists(route_matcher):
    try:
        assert route_matcher("/download/kenzie.png")
    except NotFound:
        fail('Verifique se a rota "/download" existe')
    except InternalServerError:
        fail(
            'Seu servidor está com erro interno na rota "/download", essa rota não é capaz de processar uma requisição'
        )


def test_route_download_zip_exists(route_matcher):
    try:
        assert route_matcher("/download-zip")
    except NotFound:
        fail('Verifique se a rota "/download-zip" existe')
    except InternalServerError:
        fail(
            'Seu servidor está com erro interno na rota "/download-zip", essa rota não é capaz de processar uma requisição'
        )


# def test_route_upload_exists(route_matcher):
#     try:
#         assert route_matcher("/upload")
#     except NotFound:
#         fail('Verifique se a rota "/upload" existe')
#     except InternalServerError:
#         fail(
#             'Seu servidor está com erro interno na rota "/upload", essa rota não é capaz de processar uma requisição'
#         )

