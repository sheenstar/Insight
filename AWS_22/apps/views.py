from a_model import ModelIt
from flask import render_template
from flask import request
from apps import app
import pandas as pd
import gzip
import dill
import pickle
import json
import plotly
import numpy as np
import plotly.tools as tls


with gzip.open('percent_rmse.dill.gz', 'r') as ff:
   rmse_test = dill.load(ff)

with gzip.open('state_model_aves.dill.gz', 'r') as gg:
   state_model_aves = dill.load(gg)   

with gzip.open('important_features.dill.gz', 'r') as fff:
   important_features = dill.load(fff)

with gzip.open('insights.dill.gz', 'r') as hh:
   insights = dill.load(hh)

with gzip.open('error_percentile.dill.gz', 'r') as rr:
   error_percentile = dill.load(rr)

with gzip.open('readm_percentile.dill.gz', 'r') as zz:
   readm_percentile = dill.load(zz)

tls.set_credentials_file(username='sheenas',api_key='618CQEhf8rlkmtYhNYi5')

@app.route('/')
@app.route('/index', methods=['POST'])
def index():


  return render_template('index.html')

@app.route('/input', methods=['POST'])
def cesareans_input():
  return render_template("input.html")

@app.route('/output', methods=['POST'])
def cesareans_output():
  form2 = request.form
  value = form2['state_abbrev']
  #pull 'birth_month' from input field and store it
  output = rmse_test[value]
  output1 = state_model_aves[value]
  output2 = important_features[value][0]
  output3= important_features[value][1]
  output4= important_features[value][2]
  output5= insights[value][0]
  output6= error_percentile[value]
  output7 = readm_percentile[value]
  return render_template("output.html", value=value, the_result = output, the_result1 = output1, 
    the_result2 = output2, the_result3 = output3, the_result4 = output4, the_result5 = output5,
    the_result6 = output6, the_result7 = output7)