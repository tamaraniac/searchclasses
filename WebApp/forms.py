from flask_wtf import Form
from wtfforms import StringField, BooleanField
from wtfforms.validators import DataRequired

class Specifications(Form):
    term = StringField('term', validators=[DataRequired()])
    year = StringField('year', validators=[DataRequired()])
    department = StringField('department')
    coursenumber = StringField('coursenumber')
    department = StringField('department')
    gened1 = StringField('gened1')
    gened2 = StringField('gened2')
    gened3 = StringField('gened3')
    allcat = BooleanField('allcat', default=true)
    anycat = BooleanField('anycat', default=false)
    mon = BooleanField('mon', default=false)
    tue = BooleanField('tue', default=false)
    wed = BooleanField('wed', default=false)
    thur = BooleanField('thur', default=false)
    fri = BooleanField('fri', default=false)
    sat = BooleanField('sat', default=false)
    sun = BooleanField('sun', default=false)
    earliesttime = StringField('earliesttime')
    latesttime = StringField('latesttime')
    breakstart = StringField('breakstart')
    breakend = StringField('breakend')
    mainquad = BooleanField('mainquad', default=false)
    south = BooleanField('south', default=false)
    bardeen = BooleanField('bardeen', default=false)
    north = BooleanField('north', default=false)
