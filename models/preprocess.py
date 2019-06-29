from tensorflow.python.keras.preprocessing import image as kp_image
from load_image import load_img
import tensorflow as tf
from tensorflow.python.keras.preprocessing import image as kp_image

def load_and_process_img(path_to_img):
    img = load_img(path_to_img)
    img = tf.keras.applications.vgg19.preprocess_input(img)
    return img