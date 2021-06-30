from flask import Flask, render_template, request
import numpy as np
from joblib import load
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import uuid

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type = request.method
    if request_type == 'GET':
        return render_template('index.html', href='static/base.png')
    else:
        text = request.form['text']
        model = load('app/model.joblib')
        np_arr = floats_string_to_np_arr(text)
        random_string = uuid.uuid4().hex
        path = "app/static/" + random_string + ".svg"
        make_picture('app/AgesAndHeights.pkl', model, np_arr, path)
        return render_template('index.html', href=path[4:])

def make_picture(training_data_filename, model, new_inp_np_arr, output_file):
  data = pd.read_pickle(training_data_filename)
  ages = data["Age"]
  data = data[ages > 0]
  ages = data["Age"]
  heights = data["Height"]

  x_new = np.array(list(range(19))).reshape(19, 1)
  preds = model.predict(x_new)


  fig = px.scatter(x=ages, y=heights, title="Height VS Age of People", labels={'x': "Ages (years)", "y": "Heights (inches)"})

  fig.add_trace(go.Scatter(x=x_new.reshape(19), y=preds, mode='lines', name='Model'))

  new_preds = model.predict(new_inp_np_arr)

  fig.add_trace(go.Scatter(x=new_inp_np_arr.reshape(len(new_inp_np_arr)), y=new_preds, mode='markers', name='New Output', marker=dict(color='purple', size=20, line=dict(color='purple'))))

  fig.write_image(output_file, width=800, engine='kaleido')

def floats_string_to_np_arr(floats_str):
  def is_float(s):
    try:
      float(s)
      return True
    except:
      return False
  floats = np.array([float(x) for x in floats_str.split(',') if is_float(x)])
  return floats.reshape(len(floats), 1)