<!DOCTYPE html>
<html lang="en">
<head>

    <title>Virtual Artist - A Style Transfer Web App</title>

</head>
<body>

    <div class="header">
        <h1>Virtual AI Artist</h1>
        <h3>A Machine Learning Style Transfer Web App</h3>
    </div>
      
    <div class="container-fluid">

        <div class="navbar">
            <a href="#" class="active">Home</a>
            <a href="#">Form</a>
            <a href="#">Result</a>
            <a href="#" class="right">About Style Transfer</a>
          </div>
          
  


              <!-- php to save images -->
              <?php
              $info = pathinfo($_FILES['userFile']['name']);
              $ext = $info['extension']; // get the extension of the file
              $newname = "newname.".$ext; 

              $target = 'images/'.$newname;
              move_uploaded_file( $_FILES['userFile']['tmp_name'], $target);
              ?>

              <!-- fimal submit -->
              <form action="add.php">
                <input type="submit">
              </form>
              <br>
              <h2>Result Image</h2>
              <h5>After training the result showed this</h5>
              <div class="fakeimg" style="height:200px;">Image</div>
              <p>Some text..</p>
              <p>Sunt in culpa qui officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.</p>
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