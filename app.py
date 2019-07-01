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
    flash,
    redirect,
    url_for,
    session,
    render_template,
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

        if request.files.get('style'):
            # read the file
            file = request.files['style']
            print(file)
            # read the filename
            filename = file.filename
            

            # Save the file to the uploads folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        if request.files.get('content'):
            # read the file
            file = request.files['content']
            print(file)
            # read the filename
            contentfilename = file.filename

            # Save the file to the uploads folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], contentfilename))
            return render_template("index.html")

    return render_template("form.html")
# @app.route("/upload")
# def init():
#     try:
#         # Use Pandas to perform the sql query
#         time_stmt = db.session.query(initTime).statement
#         time_df = pd.read_sql_query(time_stmt, db.session.bind)
#         time_data = {
#             "content": time_df.date.values.tolist(),
#             "style": time_df.tacos.values.tolist(),
#             "qualirt": time_df.sandwiches.values.tolist(),

#         }

#         session['keywords'] = ['tacos','sandwiches','kebabs']

#         # Results
#         return jsonify(time_data)
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template(".html",result = result)

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

