from selenium import webdriver
import requests
import io
from PIL import Image
#PATH = 
wb = webdriver.Chrome(PATH)

image_url = "https://ichef.bbci.co.uk/news/976/cpsprodpb/17638/prkduction/_124800859_gettyimages-817514614.jpg"

def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name
        
        with open(file_path, "wb") as f:
            image.save(f, "JPEG")
            
        print("Success")
    except Exeption as e:
        print('Failed -', e)
download_image("", image_url, "test.jpg")