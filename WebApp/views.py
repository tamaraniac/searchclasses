from flask import render_template, flash, redirect
from .forms import Specifications
from WebApp import app

@app.route('/')
def index():

@app.route('/coursesearch', methods=['GET', 'POST'])
def CoursesForm():
    form = Specifications()
    if form.validate_on_submit():
        flash() #use this to display results
    return render_template('form.html' title = 'Course Search', form=form)
