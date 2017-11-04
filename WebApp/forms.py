from flask_wtf import Form
from wtfforms import StringField, BooleanField, SelectField
from wtfforms.validators import DataRequired

class Specifications(Form):
    term = StringField('term', validators=[DataRequired()])
    year = StringField('year', validators=[DataRequired()])
    department = StringField('department')
    coursenumber = StringField('coursenumber')
    gened1 = SelectField('gened1', choices = [('', ''), ('AC', 'Advanced Composition'),
    ('W', 'Western / Comparitive Cultures'), ('NW', 'Non-Western / US Minority Cultures'),
    ('HA', 'Humanities and the Arts'), ('NST', 'Natural Sciences and Technology'),
    ('QR', 'Quantitive Reasoning'), ('SBS', 'Social and Behavioral Sciences')])
    gened2 = SelectField('gened2', choices = [('', ''), ('AC', 'Advanced Composition'),
    ('W', 'Western / Comparitive Cultures'), ('NW', 'Non-Western / US Minority Cultures'),
    ('HA', 'Humanities and the Arts'), ('NST', 'Natural Sciences and Technology'),
    ('QR', 'Quantitive Reasoning'), ('SBS', 'Social and Behavioral Sciences')])
    gened3 = SelectField('gened3', choices = [('', ''), ('AC', 'Advanced Composition'),
    ('W', 'Western / Comparitive Cultures'), ('NW', 'Non-Western / US Minority Cultures'),
    ('HA', 'Humanities and the Arts'), ('NST', 'Natural Sciences and Technology'),
    ('QR', 'Quantitive Reasoning'), ('SBS', 'Social and Behavioral Sciences')])
    allorany = SelectField('allorany' choices = [('all', 'All'), ('any', 'Any')])
    mon = BooleanField('mon', default=false)
    tue = BooleanField('tue', default=false)
    wed = BooleanField('wed', default=false)
    thur = BooleanField('thur', default=false)
    fri = BooleanField('fri', default=false)
    earliesttime = StringField('starttime')
    latesttime = StringField('latesttime')
    breakstart = StringField('breakstart')
    breakend = StringField('breakend')
    mainquad = BooleanField('mainquad', default=false)
    south = BooleanField('south', default=false)
    bardeen = BooleanField('bardeen', default=false)
    north = BooleanField('north', default=false)
