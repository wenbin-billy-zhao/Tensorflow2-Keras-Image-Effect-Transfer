import os
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (10,10)
mpl.rcParams['axes.grid'] = False

import numpy as np
from PIL import Image # pillow for image manipulation
import time
import functools

from load_image import load_image
from image_show import image_show

def show_results(best_img, content_path, style_path, show_large_final=True):
    plt.figure(figsize=(10, 5))
    content = load_image(content_path) 
    style = load_image(style_path)

    plt.subplot(1, 2, 1)
    image_show(content, 'Content Image')

    plt.subplot(1, 2, 2)
    image_show(style, 'Style Image')



    if show_large_final: 
        plt.figure(figsize=(10, 10))

        plt.imshow(best_img)
        plt.title('Output Image')
        imwrite(best_img, '../static/output_images/output.jpg')
        plt.show()