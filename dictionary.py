# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 16:55:23 2020

@author: naona
"""

from PyDictionary import PyDictionary
import pyperclip
from plyer import notification
import time
from googletrans import Translator

"""
def gets(text):
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
            #img.save('test.ico',format = 'ICO', sizes=[(128,128)])

    
    num = 1
    data = text
    for _ in range(int(num)):
        link = image(data)
        download_img(link, "test")
    
"""

import math
translator = Translator()

def mid(text, n, m):
  return text[n-1:n+m-1]

dictionary=PyDictionary()
text = 0
skip = 0
text = pyperclip.paste()
print(text)
for timing in range(20000):
    text1 = pyperclip.paste()
    if text1 == text:
        pass 
    else:
        if text == 0:
            skip = 1
        else:
            text = text1
            
        if len(text.split(" ")) >=3:
            print(text)
            meaning = translator.translate(text, src='en', dest='ja').text
            print(meaning)
            k = 0
        else:
            meaning = dictionary.meaning(text)
            k = 1
            
            
            
        if meaning == None:
            #notification.notify(
            #    title="エラー",
            #    message="読み取れませんでした",
            #   app_name='English Dictionary',
            #     )
            ttt = 0
        else:
            print(meaning)
            if skip == 1:
                pass
            #gets(text)
            if k == 0:
                title = "translation"
            else:
                title = text
            print(len(meaning))
            if (len(meaning) >= 400):
                ttt = 1
            elif (len(meaning) >= 100 and len(meaning) <= 400):
                first = 0
                end = 100
                lengthi = math.ceil(len(meaning) / 100)
                print(lengthi)
                for num in range(lengthi):
                    notification.notify(
                        title=title,
                        message=meaning[first:end],
                        app_name='English Dictionary',
                        timeout=100
                        #app_icon="test.ico"
                        )    
                    first += 101
                    end += 101            
            else:
                notification.notify(
                    title=title,
                    message=meaning,
                    app_name='English Dictionary',
                    timeout=100
                    #app_icon="test.ico"
                    )
    time.sleep(1.0)
    
    


        
    


