from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit
import cv2
from PIL import Image
import io
import numpy as np
import imutils
import base64
from find_phone import find_phone
from eye_track import eyes_are_closed
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)
app.static_folder = 'static'
socketio = SocketIO(app,cors_allowed_origins='*')

global imageCount
imageCount = 1


@socketio.on('image')
def image(data_image):
    sbuf = io.StringIO()
    sbuf.write(data_image)

    # decode and convert into image
    b = io.BytesIO(base64.b64decode(data_image))
    pimg = Image.open(b)

    stream = io.BytesIO()
    pimg.save(stream, format='PNG') # convert PIL Image to Bytes
    bin_img = stream.getvalue()

    #Detect Phone Usage
    phone_status = find_phone(bin_img)

    #Detect Eyes
    eye_closed = eyes_are_closed(bin_img)

    # emit the frame back
    emit('response_back', [phone_status, eye_closed])

@socketio.on('get_data')
def get_data(dict_data):
  global imageCount
  sns.set_theme()
 
  # Data
  min_length = min(min(len(dict_data['tabData']), len(dict_data['phoneData'])), len(dict_data['eyeData']))
  y=[[x*100/3 for x in dict_data['tabData'][:min_length]], [x*100/3 for x in dict_data['phoneData'][:min_length]], [x*100/3 for x in dict_data['eyeData'][:min_length]]]

  x=list(range(0,len(y[0]))) 
  print(x,y)
  # Plot
  plt.stackplot(x,y[0],y[1],y[2], labels=['Tab Focus','Phone','Sleep'])
  plt.legend(loc='upper left')

  plt.title('Total Overview of Productivity')
  plt.xlabel('Time')
  plt.ylabel('Stacked Percentage of Undistracted Time')
  
  imageCount += 1
  plt.savefig(f'static/test{imageCount}.jpg')
  plt.close()
  emit('redirect', f'/summary?count={imageCount}')

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route("/camera", methods=['POST', 'GET'])
def camera():
  return render_template("camera.html")


@app.route("/summary", methods=['POST', 'GET'])
def summary():
  count = request.args['count']
  return render_template("summary.html", count=count)

if __name__ == '__main__':
#    app.run( # Starts the site
#    host='0.0.0.0',  
#    port=2000
#    )
    socketio.run(app, host="0.0.0.0")
