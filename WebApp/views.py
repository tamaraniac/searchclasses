from flask import render_template, flash, redirect
from .forms import Specifications
from . import app
from .search import search

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
        daysOfTheWeek = ''
        if mon:
            daysOfTheWeek += 'M'
        if tue:
            daysOfTheWeek += 'T'
        if wed:
            daysOfTheWeek += 'W'
        if thur:
            daysOfTheWeek += 'R'
        if fri:
            daysOfTheWeek += 'F'
        gened = [gened1, gened2, gened3]

        classList = search(term, year, department, coursenumber, daysOfTheWeek, earliesttime, latesttime, breakstart, breakend, gened)
        return redirect('/result/<classList>')
    return render_template('form.html', title='Course Search', form=form)

@app.route('/result/<classList>')
def showResult(classList):
    return render_template('result.html', classlist=classList)
