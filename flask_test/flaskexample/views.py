from a_model import ModelIt
from flask import render_template
from flask import request
from flaskexample import app
import pandas as pd
import gzip
import dill
import pickle

with gzip.open('state_model_aves.dill.gz', 'r') as ff:
   state_aves = dill.load(ff)

with gzip.open('important_features.dill.gz', 'r') as fff:
   important_features = dill.load(fff)


@app.route('/')
@app.route('/index', methods=['POST'])
def index():
    return render_template("index.html")

@app.route('/input', methods=['POST'])
def cesareans_input():
    return render_template("input.html")

@app.route('/output', methods=['POST'])
def cesareans_output():
  form2 = request.form
  value = form2['state_abbrev']
  #pull 'birth_month' from input field and store it
  output = state_aves[value]
  output1 = important_features[value]
  return render_template("output.html", the_result = output, the_result1 = output1)