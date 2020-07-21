# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:28:16 2020

@author: DELL
"""

from flask import Flask

app=Flask(__name__)
@app.route('/')
def hello():
    return("welcome Interns")
    
@app.route('/whatnext/')
def next():
    return("Project development")
    
if __name__ =='__main__' :
    app.run(debug=True)
    