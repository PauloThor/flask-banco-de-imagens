from flask import Flask, request, send_from_directory, jsonify
from environs import Env
from os import environ, system
from operations.image import create_files, check_file_error, save_file, get_all_files, get_files_by_type, get_path
env = Env()
env.read_env()

app = Flask(__name__)

create_files()
max_content = environ.get('MAX_CONTENT_LENGTH')


@app.route("/upload", methods=["POST"])
def post_file():

    try:
        selected_file = request.files['file']

        error = check_file_error(selected_file)

        if error['error'] == 'yes':
            return {"message": error['message']}, error['type']

        save_file(selected_file)
        # selected_file.save('./kenzie.png')

        return {"message": selected_file.filename}, 201

    except Exception:
        return {"message": "Upload mal sucedido."}, 404


@app.route('/files')
def list_files():
    try:
        output = get_all_files()
        return jsonify(output), 200

    except Exception:
        return '', 404


@app.route('/files/<tipo>')
def list_files_by_type(tipo: str):

    try:
        output = get_files_by_type(tipo)
        return jsonify(output), 200

    except Exception:
        return '', 404


@app.route('/download/<file_name>')
def download(file_name):

    try:
        final_path = get_path(file_name)

        return send_from_directory(
            directory=final_path,
            path=file_name,
            as_attachment=True), 200

    except Exception:
        return {"message": "O arquivo não existe."}, 404


@app.route('/download-zip')
def download_zip():
    file_type = request.args.get('file_type')
    compression_rate = request.args.get('compression_rate')

    system(f'zip {compression_rate} -r zipped ../files/{file_type}')

    return compression_rate, 200
