import os
import json
import glob
import pandas as pd
import numpy as np
import time
import tensorflow as tf
import tensorflow.contrib.eager as tfe
from random import shuffle

from stm_model import StyleTransferModel
import transfer_tools as tt

from flask import (
    Flask,
    session,
    render_template,
    jsonify,
    url_for, 
    request, 
    redirect
    )

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'
app.config['UPLOAD_FOLDER'] = 'uploads'

# enable eager execution
tf.enable_eager_execution()
print("Eager execution: {}".format(tf.executing_eagerly()))

#Ran this only once to save the model to a json file.
#tt.save_vgg_to_file()

stm = StyleTransferModel()

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")


@app.route("/run_transfer", methods=['GET'])
def run_transfer(inputValue):
    content_path  = request.args.get('content-path', None)
    style_path  = request.args.get('style-path', None)
    best, best_loss = stm.run_style_transfer(content_path, 
                                     style_path, num_iterations=3)


if __name__ == "__main__":
    app.run(debug=True)

