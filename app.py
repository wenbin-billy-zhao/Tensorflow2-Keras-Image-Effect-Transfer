import os
import pandas as pd
import numpy as np
import time
import tensorflow as tf
import tensorflow.contrib.eager as tfe

from transfer_tools import (
    run_style_transfer
)

import json

from flask import (
    Flask,
    flash,
    redirect,
    url_for,
    session,
    render_template,
    send_from_directory,
    jsonify,
    request)

from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'
app.config['UPLOAD_FOLDER'] = 'uploads'

# read in csv
art_df = pd.read_csv("static/csv/artist_and_art_titles.csv")

# enable eager execution
tf.enable_eager_execution()
print("Eager execution: {}".format(tf.executing_eagerly()))


#################################################
# Flask Routes
#################################################

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/",  methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request)
        # get quality
        data = request.form['quality']
        # get style
        if request.files.get('style'):
            file = request.files['style']
            print(file)
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # get content
        if request.files.get('content'):
            file = request.files['content']
            print(file)
            contentfilename = file.filename

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], contentfilename))
            try:
                return render_template("index.html", contentfilename =( f'uploads/{contentfilename}'), filename=(f'uploads/{filename}'), quality=data)
            except: 
                return render_template("index.html", contentfilename = ( f'uploads/{contentfilename}'))

    return render_template("form.html")
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template(".html",result = result)

@app.route("/art_data")
def data():
    art_data = {
        "art_image": art_df.Art_Piece.values.tolist(),
        "art_title": art_df.Piece_Title.values.tolist(),
        "artist": art_df.Artists.values.tolist()
        }
    return jsonify(art_data)

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/run_transfer")
def run_transfer(inputValue):
    content_path  = request.args.get('content-path', None)
    style_path  = request.args.get('style-path', None)
    iterations = request.args.get('quality', None)

    # Content layer where will pull our feature maps
    content_layers = ['block5_conv2'] 

    # Style layer we are interested in
    style_layers = ['block1_conv1',
                    'block2_conv1',
                    'block3_conv1', 
                    'block4_conv1', 
                    'block5_conv1'
               ]

    best, best_loss = run_style_transfer(content_path, 
                                     style_path, num_iterations=3)


if __name__ == "__main__":
    app.run(debug=True)

