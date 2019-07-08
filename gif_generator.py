import imageio
import os

def gif_generator():
    list_of_files = os.listdir('static/12-iterations/')
    list_of_files.pop(0) # remove first DS
    full_path = ["static/12-iterations/{0}".format(x) for x in list_of_files]
    images = []
    for filename in full_path:
        images.append(imageio.imread(filename))
    imageio.mimsave('static/gif/recent.gif', images)