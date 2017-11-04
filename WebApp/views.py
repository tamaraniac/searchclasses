from flask import render_template, flash, redirect
from .forms import Specifications
from WebApp import app

@app.route('/')
def index():
    

def specifications():
    form = Specifications()
    return render_template('form.html' title = 'Course Search', form=form)
