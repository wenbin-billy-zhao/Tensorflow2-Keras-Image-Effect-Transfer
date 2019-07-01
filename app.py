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

    return '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous"> -->
    <link rel="stylesheet" href="../static/css/bootstrap.min.css"><!-- custom bootstrap theme css, for reference: https://bootswatch.com/sketchy/ -->
    <link rel="stylesheet" href="../static/css/style.css">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <title>Virtual Artist - A Style Transfer Web App</title>
    
    <script class="jsbin" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
    <script class="jsbin" src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.0/jquery-ui.min.js"></script>

</head>
<body>

    <div class="header" href="/">
        <h1>Virtual AI Artist</h1>
        <h3>A Machine Learning Style Transfer Web App</h3>
    </div>

    <div class="container-fluid">
          
          <div class="row">
            <div class="side">
              <!-- iterations -->
              <h2>Quality</h2>
              <p>Select the quality of the transfer you'd like</p>
              <div class="iterations" style="height:60px;">
                
                <button>Low</button>
                <button>Moderate</button>
                <button>High</button>
              </div>          
              <br>      
              <h2>Select Your Style</h2>
              <p>Select fro our library or load your own!</p>

              <br>
              <!-- <input type="submit"> -->
              <!-- Artists selection dropdown -->
              <div class="btn-group">
                <button type="button" class="btn btn-danger dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  Art Library
                </button>
                <div class="dropdown-menu">
                  <a class="dropdown-item" href="#">Artist</a>
                  <a class="dropdown-item" href="#">Art Title</a>
                  <a class="dropdown-item" href="#">Art Work</a>
                  <div class="dropdown-divider"></div>
                  <a class="dropdown-item" href="#">
                        <form method=post enctype=multipart/form-data >
                    <input type='file' onchange="readURLstyle(this);" name="style"/>
                    <img id="style-image" src="#" alt="" />
                    </a>
                </div> <!--dropdown-menu-->
              </div> <!--btn-group-->
              

              <!-- End of artist selection dropdown -->
              <!-- style image display -->
              <div class="style_image">
                <img class = "image" id="style-place-holder" src="https://uploads4.wikiart.org/images/rembrandt/christ-in-the-storm-1633.jpg!PinterestSmall.jpg" alt=""> 
              </div>
            </div>
            
            <div class="main">
              <h2>Upload Your Desired Image</h2>
              <h5>Target image for rendering</h5>
              <!-- content show image upon upload -->
              
                <input type='file' onchange="readURLcontent(this);" name="content" />
                <br>
                <img id="content-image" src="#" alt="" />
                <br>
              
              <!--content image display -->
              <div class="content-place-holder" >
                  <img id="content-place-holder" src="../static/content_images/archway.jpeg" alt="">
              </div>
                <input type=submit value=Upload>
              </form>            
            </div>
          </div>

    </div>  
      
    <div class="footer">
      <h4>&copy;2019 - The Minority Majority Team</h4>
      <p>Credit and Sighitings: reference to sites and github repos</p>
    </div>  

    <script type="text/javascript" src="static/js/logic.js"></script>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
    '''
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

