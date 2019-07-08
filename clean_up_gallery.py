# libraries
import os

def cleaning():
    list_of_files = os.listdir('static/gallery/')
    list_of_files.pop(0) # remove first DS
    full_path = ["static/gallery/{0}".format(x) for x in list_of_files]
    print(full_path)
    if len([name for name in list_of_files]) > 12:
        oldest_file = min(full_path, key=os.path.getctime)
        print(oldest_file)
        os.remove(oldest_file)
    elif len([name for name in list_of_files]) == 12 or len([name for name in list_of_files]) < 12:
        print(f'There are {len([name for name in list_of_files])} files in the gallery folder. \nNo deletion required.')
    return list_of_files

def pull_files():
    list_of_files = os.listdir('static/gallery/')
    list_of_files.pop(0) # remove first DS
    full_path = ["static/gallery/{0}".format(x) for x in list_of_files]
    return full_path