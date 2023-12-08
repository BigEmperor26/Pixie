# image library
from PIL import Image

import numpy as np
import matplotlib.pyplot as plt
class Pixie:
    def __init__(self, image:str) -> None:
        img = Image.open(image)
        self.img = img.convert('RGB')
        self.width, self.height: (int,int) = self.img.size
        self.pixels = self.img.load()
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
if __name__ == '__main__':
    # open image
    pixie = Pixie('img.png')
    # resize image
    pixie.img = pixie.resize(pixie.img, 100, 100)
    # show image
    pixie.pixellate(pixie.img, 10).show()