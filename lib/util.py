import os
import subprocess


def get_api_key():
    return os.environ.get('PIX_KEY')


def get_screen_resolution():
    return subprocess.Popen(r'xrandr | grep "\*" | cut -d" " -f4', shell=True, stdout=subprocess.PIPE).communicate()[0].decode("utf-8").replace('\n','').split('x')

def create_folder(path):
    pass

def check_file_exits(file_path):
    pass

def delete_file(file_path):
    pass            