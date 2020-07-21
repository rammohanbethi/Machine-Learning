# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:08:06 2020

@author: HP
"""

from flask import Flask, redirect, url_for, request
app= Flask(__name__)

@app.route('/sucess/<name>')
def success(name):
    return "Welcome %s" % name

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        user=request.form['nm']
        return redirect(url_for('success',name=user))
    else:
        user=request.args.get('nm')
        return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)