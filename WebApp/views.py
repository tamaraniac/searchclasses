from flask import render_template, flash, redirect
from .forms import Specifications
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/coursesearch', methods=['GET', 'POST'])
def CoursesForm():
    form = Specifications()
    if request.method == 'POST':
        if form.validate() == False:
            flash('Some fields are required')
            return render_template('form.html', title = 'Course Search', form=form)
        else:
            return render_template('result.html')
    elif request.method == 'GET':
        return render_template('form.html', title = 'Course Search', form=form)
