# import tensor flow for machine learning
import tensorflow as tf
import tensorflow.contrib.eager as tfe

from tensorflow.python.keras.preprocessing import image as kp_image
from tensorflow.python.keras import models 
from tensorflow.python.keras import losses
from tensorflow.python.keras import layers
from tensorflow.python.keras import backend as K

def get_content_loss(base_content, target):
    return tf.reduce_mean(tf.square(base_content - target))