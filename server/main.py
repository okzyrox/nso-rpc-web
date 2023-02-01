from flask import Flask, render_template, redirect, url_for

import os, sys, requests, time, datetime, json

import api


app = Flask(__name__)

FrontendTimeStart = time.time() # frontend

@app.route("/")
def home():

    FrontendTimeElapsedEp = time.time() - FrontendTimeStart # fetch epoch time elapsed

    FrontendTimeElapsed = time.strftime("%H:%M:%S", time.gmtime(FrontendTimeElapsedEp)) # convert epoch to H:M:S

    ctx = {
        'FrontendTime':FrontendTimeElapsed
    }



    return render_template('index.html', **ctx) # '**' makes it so we dont have to write "ctx." in each template

app.route('/u/')
@app.route('/u/<id>')
def user(id=None):

    if id == None:
        return redirect(url_for('404'))
    else:

        ctx = {
            'uid':id
        }

        return render_template('user.html', **ctx)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error/404.html'), 404
