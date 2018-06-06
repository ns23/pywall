from lib import pywallib
from os import getcwd
from time import sleep


def main(run_forever=True):
    while run_forever:
        image_dict = pywallib.get_images()
        selected_image = pywallib.select_image(image_dict)
        img_name = "{}.jpg".format(selected_image['id'])
        download_img = pywallib.download_image(
            selected_image['largeImageURL'], name=img_name)

        if download_img:
            pywallib.set_wallpaper('{}/{}'.format(getcwd(), img_name))
        else:
            print('Was not able to download the image,Please try again')
        
        sleep(900)    


main()
