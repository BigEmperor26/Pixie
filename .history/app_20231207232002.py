# image library
from PIL import Image
from PIL.Image import Image as PILImage

import numpy as np
import matplotlib.pyplot as plt
class Pixie:
    @staticmethod
    def resize ( img:Image.Image, width, height):
        """
        Resize image
        :param img: Image
        """
        img = img.resize((width, height))
        return img
    @staticmethod
    def scale ( img:Image.Image, factor):
        """
        Scale image
        :param img: Image
        """
        img = img.resize((int(img.width * factor), int(img.height * factor)))
        return img
    @staticmethod
    def blur( img:Image.Image, pixel_size):
        """
        Blur image
        :param img: Image
        """
        img = Pixie.scale(img,1 / pixel_size)
        img = Pixie.scale(img,pixel_size)
        return img
    @staticmethod
    def pixellate( img:Image.Image, pixel_size):
        """
        Pixellate image
        :param img: Image
        """
        np_img = np.array(img)
        h,w,c = np_img.shape
        new_h = h // pixel_size
        new_w = w // pixel_size
        
        new_np_img = np.zeros((new_h,new_w,c),dtype = np.uint8)
        # loop through pixels
        for c in range(np_img.shape[-1]):
            for i in range(new_h):
                for j in range(new_w):
                    # get pixel value
                    pixel = np_img[i,j,c]
                    # set pixel value
                    new_np_img[i,j,c] = pixel
        import pdb; pdb.set_trace()
        new_img = Image.fromarray(new_np_img) 
        return new_img
    @staticmethod
    def colorize( img:Image.Image, colors):
        """
        Colorize image
        :param img: Image
        """
        img = img.convert('P', palette=Image.ADAPTIVE, colors=colors)
        img = img.convert('RGB')
        return img
if __name__ == '__main__':
    # open image
    img = Image.open('img.png')
    # resize image
    # show image
    pixellated = Pixie.pixellate(img, 100)
    pixellated.show()
    colorized = Pixie.colorize(pixellated, 10)
    colorized.show()