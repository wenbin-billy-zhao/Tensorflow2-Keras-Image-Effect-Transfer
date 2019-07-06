import os
import pandas as pd
import numpy as np
import time
import tensorflow as tf
import tensorflow.contrib.eager as tfe

from transfer_tools import (
    run_style_transfer
)

from flask import (
    Flask,
    session,
    render_template,
    jsonify)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'

# enable eager execution
tf.enable_eager_execution()
print("Eager execution: {}".format(tf.executing_eagerly()))


#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")


@app.route("/run_transfer")
def run_transfer(inputValue):
    content_path  = request.args.get('content-path', None)
    style_path  = request.args.get('style-path', None)

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

