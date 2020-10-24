# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 22:36:37 2020

@author: naona
"""
import requests
import random
import shutil
import bs4
import ssl
import os
from PIL import Image

def gets():
    ct = os.getcwd()
    path = os.path.join(ct,"test.png")
    ssl._create_default_https_context = ssl._create_unverified_context
    def image(data):
        Res = requests.get("https://www.google.com/search?hl=en&q=" + data + "&btnG=Google+Search&tbs=0&safe=off&tbm=isch")
        Html = Res.text
        Soup = bs4.BeautifulSoup(Html,'html.parser')
        links = Soup.find_all("img")
        links =links[1]
        link = links.get("src")
        return link
    def download_img(url, file_name):
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(file_name+".png", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
            img = Image.open(file_name+".png")
            img.save('test.ico',format = 'ICO', sizes=[(128,128)])

    
    num = 1
    data = "make"
    for _ in range(int(num)):
        link = image(data)
        download_img(link, "test")
    print("OK")
    
if __name__ == "__main__":
    gets()