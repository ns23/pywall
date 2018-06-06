## Pywallpaper

A simple python command line utility to download images from pixbay

## steps to create pixbay API key

* Open the link [pixbay api](https://pixabay.com/api/docs/)
* Create a account 
* Press `ctrl+f` and search `Your API key`
* Copy the API Key

## set up virtual env

Follow this github gist on how to create virtual env [gist](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)



## Set the environment variable

The pixbay APIkey is stored in environment varaible *PIX_KEY*

### Set Environment varaible on Linux

```
export PIX_KEY='<Your API key>'
```

### Set Environent varaible on Windows

```
setx PIX_KEY "<Your API key>"

```

## Install Dependancies

```bash
    pip install -r requirements.txt
```

## To run the script

```bash
python pywall.py

```