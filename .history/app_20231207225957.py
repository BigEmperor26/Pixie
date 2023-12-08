# image library
from PIL import Image

import numpy as np
import matplotlib.pyplot as plt
class Pixie:
    def resize (self, img, width, height):
        """
        Resize image
        :param img: Image
        """
        img = img.resize((width, height))
        return img
    def scale (self, img, factor):
        """
        Scale image
        :param img: Image
        """
        img = img.resize((int(img.width * factor), int(img.height * factor)))
        return img
    def pixellate(self, img, pixel_size):
        """
        Pixellate image
        :param img: Image
        """
        img = img.resize((int(img.width / pixel_size), int(img.height / pixel_size)))
        img = img.resize((img.width * pixel_size, img.height * pixel_size))
        return img
    def colorize(self, img, colors):
        """
        Colorize image
        :param img: Image
        """
        img = img.convert('P', palette=Image.ADAPTIVE, colors=colors)
        img = img.convert('RGB')
        return img
if __name__ == '__main__':
    # open image
    pixie = Pixie('img.png')
    # resize image
    # show image
    pixellated = pixie.pixellate(pixie.img, 10)
    colorized = pixie.colorize(pixellated, 10)
    colorized.show()