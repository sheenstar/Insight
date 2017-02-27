#!/usr/bin/env python


from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import TextField, IntegerField, StringField, SubmitField, SelectField, DecimalField
from wtforms.validators import Required, Optional
import numpy as np
import pandas as pd

from apps import app
app.run(debug = True)






