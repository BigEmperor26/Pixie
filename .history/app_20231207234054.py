# image library
from PIL import Image, ImageFilter

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
    def pixellate( img:Image.Image, pixel_size) -> Image.Image:
        """
        Pixellate image
        :param img: Image
        """
        np_img = np.array(img)
        h,w,c = np_img.shape
        new_h = h // pixel_size
        new_w = w // pixel_size
        
        new_np_img = np.zeros((new_h*pixel_size,new_w*pixel_size,c),dtype = np.uint8)
        # loop through pixels each channel at the time
        for c in range(np_img.shape[-1]):
            for i in range(new_h):
                for j in range(new_w):
                    # get pixel value as mean of pixel_size x pixel_size square
                    pixel = np_img[i*pixel_size:(i+1)*pixel_size,j*pixel_size:(j+1)*pixel_size,c].mean()
                    # set pixel value for pixel_size x pixel_size square
                    new_np_img[i*pixel_size:(i+1)*pixel_size,j*pixel_size:(j+1)*pixel_size,c] = pixel
        
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
    pixellated = Pixie.pixellate(img, 20)
    pixellated.show()

    # blur = Pixie.blur(img, 20)
    # blur.show()