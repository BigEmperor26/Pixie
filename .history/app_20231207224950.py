# image library
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
if __name__ == '__main__':
    # open image
    img = Image.open('img.png')
    # convert image to RGB
    img = img.convert('RGB')
    # resize image
    img = img.resize((600, 600))
    # save image
    img.save('img-resize.png')
    # show image
    img.show()