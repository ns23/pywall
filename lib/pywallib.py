import python_pixabay
import random
import urllib3
from requests import get
from lib import util, pixbay_dict
import sys
import os


def get_images(test=False):
    if test:
        return _get_images_dict()
    else:
        return _get_images_pixbay()


def _get_images_pixbay():
    screen_resoultion = util.get_screen_resolution()
    PIXBAY_API_KEY = util.get_api_key()
    pix = python_pixabay.Pixabay(PIXBAY_API_KEY)
    return pix.image_search(q='cats',
                            response_group='high_resolution',
                            category='animals',
                            min_width=screen_resoultion[1],
                            min_height=screen_resoultion[0],
                            order='latest',
                            per_page=50
                            )


def _get_images_dict():
    return pixbay_dict.get()


def select_image(image_dict):
    return image_dict['hits'][random.randint(0, 49)]


def download_image(url, name="defautlt.jpeg"):
    img_path = os.path.join(os.getcwd(),'images', name)
    print(img_path)
    try:
        if not util.check_file_exits(img_path):
            with open(img_path, "wb") as file:
                resp = get(url)
                file.write(resp.content)
                pass
        return True
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return False


def set_wallpaper(pic_path):
    if sys.platform.startswith('win32'):
        cmd = 'REG ADD \"HKCU\Control Panel\Desktop\" /v Wallpaper /t REG_SZ /d \"%s\" /f' % pic_path
        os.system(cmd)
        os.system('rundll32.exe user32.dll, UpdatePerUserSystemParameters')
        print('Wallpaper is set.')
    elif sys.platform.startswith('linux'):
        os.system(''.join(
            ['gsettings set org.gnome.desktop.background picture-uri file://', pic_path]))
        print('Wallpaper is set.')
    else:
        print('OS not supported.')
        return


def create_download_dir():
    util.create_folder(os.path.join(os.getcwd(), 'images'))
