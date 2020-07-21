# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:55:01 2020

@author: DELL
"""

from flask import Flask

app=Flask(__name__)
@app.route('/')
def hello():
    return("welcome Interns sb ")
    
if __name__ =='__main__' :
    app.run()