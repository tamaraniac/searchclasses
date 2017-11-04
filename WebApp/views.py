from flask import render_template, flash, redirect
from .forms import Specifications

def specifications():
    form = Specifications()
    return render_template('form.html' title = 'Course Search', form=form)
