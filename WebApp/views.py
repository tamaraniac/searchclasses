from flask import render_template, flash, redirect
from .forms import Specifications
from . import app

#@app.route('/')
#def index():
#    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def CoursesForm():
    form = Specifications()
    if form.validate_on_submit():
        term = form.term.data
        year = form.year.data
        department = form.department.data
        coursenumber = form.coursenumber.data
        gened1 = form.gened1.data
        gened2 = form.gened2.data
        gened3 = form.gened3.data
        allorany = form.allorany.data
        mon = form.mon.data
        tue = form.tue.data
        wed = form.wed.data
        thur = form.thur.data
        fri = form.fri.data
        earliesttime = form.earliesttime.data
        latesttime = form.latesttime.data
        breakstart = form.breakstart.data
        breakend = form.breakend.data
        mainquad = form.mainquad.data
        south = form.south.data
        bardeen = form.bardeen.data
        north = form.north.data
    return render_template('form.html', title='Course Search', form=form)
