from flask_wtf import Form
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import DataRequired

WTF_CSRF_ENABLED = False;

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
    allorany = SelectField('allorany', choices = [('all', 'All'), ('any', 'Any')])
    mon = BooleanField('mon', default=False)
    tue = BooleanField('tue', default=False)
    wed = BooleanField('wed', default=False)
    thur = BooleanField('thur', default=False)
    fri = BooleanField('fri', default=False)
    earliesttime = StringField('starttime')
    latesttime = StringField('latesttime')
    breakstart = StringField('breakstart')
    breakend = StringField('breakend')
    mainquad = BooleanField('mainquad', default=False)
    south = BooleanField('south', default=False)
    bardeen = BooleanField('bardeen', default=False)
    north = BooleanField('north', default=False)
