#!/usr/bin/env python
# coding: utf-8

# import tensor flow for machine learning
import tensorflow as tf
from tensorflow.python.keras.preprocessing import image as kp_image
from tensorflow.python.keras import Model, models, losses, layers
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.models import model_from_json
import tensorflow.contrib.eager as tfe

from keras.layers import Dense, Flatten, Dropout
from keras.callbacks import ModelCheckpoint

import numpy as np
from PIL import Image
import time
import functools
import transfer_tools as tt

import IPython.display

class StyleTransferModel:
    
    ###########################################################################

    def __init__(self):

        """ Creates our model with access to intermediate layers. 

        This function will load the VGG19 model and access the intermediate layers. 
        These layers will then be used to create a new model that will take input image
        and return the outputs from these intermediate layers from the VGG model. 

        self.model is a keras model that takes image inputs and outputs the style and 
          content intermediate layers. 
        """

        json_file = open("model.json", 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model = model_from_json(loaded_model_json)
        model.load_weights("model.h5")

        '''The model reads the raw image as input pixels and builds an internal representation through
        transformations that turn the pixels into a complex understanding of the features 
        present within the image. Convolutional neural networks capture the invariances and defining 
        features within classes (e.g., cats vs. dogs) that are agnostic to background noise and other
        nuances. It serves as a complex feature extractor; We can access intermediate layers to describe
        the content and style of input images.'''
        
        # Content layer where will pull our feature maps
        self.content_layers = ['block5_conv2'] 

        # Style layer we are interested in
        self.style_layers = ['block1_conv1',
                        'block2_conv1',
                        'block3_conv1', 
                        'block4_conv1', 
                        'block5_conv1'
                       ]

        self.num_content_layers = len(self.content_layers)
        self.num_style_layers = len(self.style_layers)
                
        self.style_outputs = [model.get_layer(name).output for name in self.style_layers]
        self.content_outputs = [model.get_layer(name).output for name in self.content_layers]
        
        self.model_outputs = self.style_outputs + self.content_outputs
        self.model = models.Model(model.input, self.model_outputs)
        
  
 
    def run_style_transfer(self, content_path, 
                           style_path,
                           num_iterations=1000,
                           content_weight=1e3, 
                           style_weight=1e-2): 
        
        # Do not train any layers of the VGG19 model, 
        # So, set trainable to false. 
        
        for layer in self.model.layers:
            layer.trainable = False
        
        """compute our content and style feature representations.

        Load and preprocess both the content and style 
        images from their path. Then feed them through the network to obtain
        the outputs of the intermediate layers. 
        
        In order to access the intermediate layers corresponding to our style and 
        content feature maps, we get the corresponding outputs by using the Keras 
        Functional API to define our model with the desired output activations.
        """
        # Load and Preprocess our images  
        content_image = tt.load_img(content_path)
        content_image = tf.keras.applications.vgg19.preprocess_input(content_image)

        style_image = tt.load_img(style_path)
        style_image = tf.keras.applications.vgg19.preprocess_input(style_image)

        # Batch compute content and style features
        style_outputs = self.model(style_image)
        content_outputs = self.model(content_image)

        # Get the style and content feature representations from our model  
        style_features = [style_layer[0] for style_layer in style_outputs[:self.num_style_layers]]
        content_features = [content_layer[0] for content_layer in content_outputs[self.num_style_layers:]]
        gram_style_features = [tt.gram_matrix(style_feature) for style_feature in style_features]

        # Set initial image
        init_image = tt.load_img(content_path)
        init_image = tf.keras.applications.vgg19.preprocess_input(init_image)
        init_image = tfe.Variable(init_image, dtype=tf.float32)
            
        # Create our optimizer
        opt = tf.train.AdamOptimizer(learning_rate=5, beta1=0.99, epsilon=1e-1)

        # For displaying intermediate images 
        iter_count = 1

        # Store our best result
        best_loss, best_img = float('inf'), None

        # Create a nice config 
        loss_weights = (style_weight, content_weight)
        cfg = {
          'model': self.model,
          'loss_weights': loss_weights,
          'init_image': init_image,
          'gram_style_features': gram_style_features,
          'content_features': content_features,
          'num_style_layers':self.num_style_layers,
          'num_content_layers':self.num_content_layers  
        }

        # For displaying
        num_rows = 2
        num_cols = 5
        display_interval = num_iterations/(num_rows*num_cols)
        start_time = time.time()
        global_start = time.time()

        norm_means = np.array([103.939, 116.779, 123.68])
        min_vals = -norm_means
        max_vals = 255 - norm_means   

        imgs = []
        for i in range(num_iterations):
            grads, all_loss = tt.compute_grads(cfg)
            loss, style_score, content_score = all_loss
            opt.apply_gradients([(grads, init_image)])
            clipped = tf.clip_by_value(init_image, min_vals, max_vals)
            init_image.assign(clipped)
            end_time = time.time() 

            if loss < best_loss:
                # Update best loss and best image from total loss. 
                best_loss = loss
                best_img = tt.deprocess_img(init_image.numpy())

            if i % display_interval== 0:
                start_time = time.time()

                # Use the .numpy() method to get the concrete numpy array
                plot_img = init_image.numpy()
                plot_img = tt.deprocess_img(plot_img)
                imgs.append(plot_img)
                IPython.display.clear_output(wait=True)
                IPython.display.display_png(Image.fromarray(plot_img))
                print('Iteration: {}'.format(i))        
                print('Total loss: {:.4e}, ' 
                    'style loss: {:.4e}, '
                    'content loss: {:.4e}, '
                    'time: {:.4f}s'.format(loss, style_score, content_score, time.time() - start_time))
        print('Total time: {:.4f}s'.format(time.time() - global_start))
        IPython.display.clear_output(wait=True)
        plt.figure(figsize=(14,4))
        for i,img in enumerate(imgs):
            plt.subplot(num_rows,num_cols,i+1)
            plt.imshow(img)
            plt.xticks([])
            plt.yticks([])

        return best_img, best_loss 

