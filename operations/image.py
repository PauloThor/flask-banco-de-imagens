from os import environ, system, listdir

all_files = listdir('../')
files_path = environ.get('FILES_DIRECTORY')
max_content = int(environ.get('MAX_CONTENT_LENGTH'))

all_types = ['png', 'jpg', 'gif']


def create_files():
    if 'files' not in all_files:
        system(f"mkdir ../{files_path}")

    type_folders = listdir(files_path)

    _ = [system(
        f'mkdir -p ../{files_path}/{folder}'
        ) for folder in all_types if folder
        not in type_folders]


def get_file_type(file_name: str):
    index = file_name.index('.') + 1
    return file_name[index:]


def check_file_size(file):
    print(file)
    size = len(file.read())

    return size > max_content


def check_file_error(file):
    size = len(file.read())
    name = file.filename
    type = get_file_type(name)

    if size > max_content:
        return {
            "error": "yes",
            "message": "Tamanho do arquivo não deve exceder 1mb!",
            "type": 413
            }

    if name in listdir(f'{files_path}/{type}'):
        return {
            "error": "yes",
            "message": "Já existe um arquivo com esse nome!",
            "type": 409
            }

    if type not in all_types:
        return {
            "error": "yes",
            "message":
            "Você deve selecionar arquivos do tipo PNG, JPG ou GIF!",
            "type": 415
        }

    return {"error": "no", "message": "none"}


def save_file(file):
    name = file.filename
    type = get_file_type(name)

    print(file)
    file.save(f'{files_path}/{type}/{name}')
    # file.save(path.join('./files/png', name))


def get_all_files():
    png_files = listdir(f'{files_path}/png')
    jpg_files = listdir(f'{files_path}/jpg')
    gif_files = listdir(f'{files_path}/gif')

    output = png_files + jpg_files + gif_files

    return output


def get_files_by_type(tipo):
    files_list = get_all_files()
    output = [file for file in files_list if get_file_type(file) == tipo]

    return output


def get_path(file_name):
    type = get_file_type(file_name)

    return f'../{files_path}/{type}'
