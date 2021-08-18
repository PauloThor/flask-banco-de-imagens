from os import environ, system, listdir
from werkzeug.utils import secure_filename

all_files = listdir('../')
files_path = environ.get('FILES_DIRECTORY')

all_types = ['png', 'jpg', 'gif']


def create_files():
    """Create all folders according to image extensions when the app starts"""

    if 'files' not in all_files:
        system(f"mkdir ../{files_path}")

    type_folders = listdir(files_path)

    _ = [system(
        f'mkdir -p ../{files_path}/{folder}'
        ) for folder in all_types if folder
        not in type_folders]


def get_file_type(file_name: str):
    """Returns the type of the file

    Args:
        file_name (str): The name of the file as a string

    Returns:
        type: The type corresponding to the file extension as a string
    """

    index = file_name.index('.') + 1
    return file_name[index:]


def check_file_error(file):
    """Returns all information about the errors of the file

    Args:
        file (dict): The file which is gonna be checked for errors

    Returns:
        dict: The dict which says if the file has an error, which error and
        what type error the route should return
    """

    name = file.filename
    type = get_file_type(name)
    files_path = environ.get('FILES_DIRECTORY')

    path_folder = listdir(f'{files_path}/{type}') 

    if name in path_folder:
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
    """Saves the file into the filers folder, on the corresponding subfolder

    Args:
        file (dict): The file which will be saved
    """

    name = secure_filename(file.filename)
    type = get_file_type(name)
    files_path = environ.get('FILES_DIRECTORY')

    print(files_path)
    file.save(f'{files_path}/{type}/{name}')
    # file.save(path.join('./files/png', name))


def get_all_files():
    """Returns all files

    Returns:
        list: The list of strings according to each file name
    """

    files_path = environ.get('FILES_DIRECTORY')

    png_files = listdir(f'{files_path}/png')
    jpg_files = listdir(f'{files_path}/jpg')
    gif_files = listdir(f'{files_path}/gif')

    output = png_files + jpg_files + gif_files

    return output


def get_files_by_type(tipo):
    """Returns a list of files according to the type

    Args:
        tipo (str): The type of the files

    Returns:
        list: The filtered list of the files according to the selected type
    """

    files_list = get_all_files()
    output = [file for file in files_list if get_file_type(file) == tipo]

    return output


def get_path(file_name):
    """Returns the path to fhe file

    Args:
        file_name (str): The name of the filed

    Returns:
        str: The path to the file
    """
    files_path = environ.get('FILES_DIRECTORY')

    type = get_file_type(file_name)

    return f'../{files_path}/{type}'
