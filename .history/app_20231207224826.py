# image library
from PIL import Image
import numpy as np

if __name__ == '__main__':
    # open image
    img = Image.open('img.jpg')
    # convert image to RGB
    img = img.convert('RGB')
    # resize image
    img = img.resize((600, 600))
    # save image
    img.save('img.jpg')
    # show image
    img.show()