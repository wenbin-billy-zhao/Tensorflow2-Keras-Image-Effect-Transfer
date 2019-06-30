# Tensorflow2-Keras-Image-Effect-Transfer
A project that utilizes Tensorflow 2 / Keras Machine Learning tools to generate a pattern/effect transfer from a model image to another


## Project Tasks and References

> I divided the tasks into a smaller bite-size functions so it can be managed by individuals. Even when they are "bite-size" these tasks will still take some time to finish. 
This list is largely sequencial, but some tasks are either run parally or can be done separately without order. 

### Front End: Flask Website
1. Build a simple unstyled page that take input and return argument to flask app
	- [ ] a. Artist/Style selector - a drop down list (we can change this later) show the list of artists complied from Jamie, once picked on-click return a value back to flask - verify result using console.log, also use flask to print out the variable choice
	
	- [ ] b. Content selector - a list of random images to be applied by style transfer - once selected, verify result by console.log - also flask print out variable
	
	- [ ] c. Submit button - that calls flask to excute style transfer (we don't have to worry about transition yet)
	
	- [ ] d. Show result images
	
	- [ ] e. decides on the web structure - root - train - result - explain - about
	
	- [ ] f. stylize the website - applying color and theme elements

---
2. Backend
	- [ ] a. build an enviornment yml file and have everyone test out that it runs both .py and .jypnb files locally
	
	- [ ] b. build flask app that runs locally, build route based on web structure (1e above)
	
	- [ ] c. build flask ->  heroku pipeline
	
	- [ ] d. we may need a database (sqlite) to host list and files - need someone explore a solution
	
	
3. Documentation and Web Content
	- [ ] a. build ReadMe file to explain the project, process
	
	- [ ] b. build presentation (we can decide the format but need someone start building, for images we can have place holders for now)
	
	- [ ] c. push out - maintian git repo
	

4. Testing and Integrating
    - [ ] a. track each tasks progress and completition, follw up with teammates for status, finding resources for help
	
	- [ ] b. testing each tasks when completed
	
	- [ ] c. organized presentation plan
	
	- [ ] d. talk with TA/instructor for additional help
	
5. Unkown / Questions
	- [ ] a. how to make style transfer go faster? (reference this site: https://reiinakano.com/arbitrary-image-stylization-tfjs/)
	
	- [ ] b. should we use vgg16 as well?
	
	- [ ] c. how to load vgg19 locally (reference this site: )?
	
Project Resources
- inspiration and credit: https://medium.com/tensorflow/neural-style-transfer-creating-art-with-deep-learning-using-tf-keras-and-eager-execution-7d541ac31398
our code is based on this article. For this notebook to work, you need tensorflow 1.10-1.13, and wget install (https://w3guy.com/wget-recognized-internal-external-command-windows-fix/)

- a newer tensorflow 2 version of above style transfer notebook is available here: 
https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/r2/tutorials/generative/style_transfer.ipynb#scrollTo=KKox7K46tKxy
though we are sticking to the first version for our project

- bootstrap theme/steyle: https://bootswatch.com/sketchy/

- alternative bootstrap themes: https://html5up.net/

- Conda enviornment management - how to create an conda enviornment for team project
	- https://gist.github.com/pratos/e167d4b002f5d888d0726a5b5ddcca57 (create environment)
	- while read requirement; do conda install --yes $requirement; done < requirements.txt (install all packages in requirements with dependencies)
	
- Manny recommanded sites for study:
   https://harishnarayanan.org/writing/artistic-style-transfer/
   https://github.com/hnarayanan/stylist/blob/master/algorithms/neural_style_transfer.ipynb

- Wenbin Zhao Billy [10:09 AM]
can you ask Manny this: so our concept is we have 3 styles on the website, then let user pick a random image or upload an image, then the website will show the process through each iteration, then present the final image
i’m trying to think what’s the best way to proceed
do we need to write javascript code to show the process? is there a off the shelf code base already available?
- Response<<
That would be cool to show the process as it steps through the iterations. There are a couple of ways to handle this. You only need to choose one of these options and the first is the one I’d recommend

  - Have a Flask endpoint that applies Style Transfer given a style and content image. You could either return a base64 representation of an array of images (an image for each iteration, see https://stackoverflow.com/questions/21227078/convert-base64-to-image-in-javascript-jquery) or save the images to a file and return the urls to the image

  - There is tensorflow.js that would keep everything in JavaScript https://reiinakano.com/arbitrary-image-stylization-tfjs/ (edited) 