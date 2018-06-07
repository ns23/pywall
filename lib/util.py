import os
import subprocess


def get_api_key():
    return os.environ.get('PIX_KEY')


def get_screen_resolution():
    return subprocess.Popen(r'xrandr | grep "\*" | cut -d" " -f4', shell=True, stdout=subprocess.PIPE).communicate()[0].decode("utf-8").replace('\n', '').split('x')


def create_folder(path):
    if not check_folder_exists(path):
        os.mkdir(path)
    else:
        print('Directory alredy exists')


def check_file_exits(file_path):
    return os.path.isfile(file_path)


def check_folder_exists(folder_path):
    return os.path.isdir(folder_path)


def delete_file(file_path):
    pass
