# image library
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
class Pixie:
    def __init__(self, image:str) -> None:
        img = Image.open(image)
        self.img = img.convert('RGB')
        self.width, self.height = self.img.size
        self.pixels = self.img.load()
        pass
    def resize (self, img, width, height):
        # convert image to RGB
        img = img.convert('RGB')
        # resize image
        img = img.resize((width, height))
        # save image
        img.save('img-resize.png')
        # show image
        img.show()
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