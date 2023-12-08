# image library
from PIL import Image

import numpy as np
import matplotlib.pyplot as plt
class Pixie:
    @staticmethod
    def resize ( img, width, height):
        """
        Resize image
        :param img: Image
        """
        img = img.resize((width, height))
        return img
    @staticmethod
    def scale ( img, factor):
        """
        Scale image
        :param img: Image
        """
        img = img.resize((int(img.width * factor), int(img.height * factor)))
        return img
    @staticmethod
    def pixellate( img, pixel_size):
        """
        Pixellate image
        :param img: Image
        """
        img = img.resize((int(img.width / pixel_size), int(img.height / pixel_size)))
        img = img.resize((img.width * pixel_size, img.height * pixel_size))
        return img
    @staticmethod
    def colorize( img, colors):
        """
        Colorize image
        :param img: Image
        """
        img = img.convert('P', palette=Image.ADAPTIVE, colors=colors)
        img = img.convert('RGB')
        return img
if __name__ == '__main__':
    # open image
    # resize image
    # show image
    pixellated = pixie.pixellate(pixie.img, 10)
    colorized = pixie.colorize(pixellated, 10)
    colorized.show()