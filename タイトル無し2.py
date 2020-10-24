# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 21:07:55 2020

@author: naona
"""
from plyer import notification
from PyDictionary import PyDictionary
dictionary=PyDictionary()

men_test = dictionary.meaning("make")
print(men_test)
print(type(men_test))
#notification.notify(title="text",message=men_test,app_name='English Dictionary',)