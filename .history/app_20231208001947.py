# image library
from PIL import Image, ImageFilter, ImageOps

import numpy as np
import matplotlib.pyplot as plt
class Pixie:
    @staticmethod
    def resize ( img:Image.Image, width, height)   -> Image.Image:
        """
        Resize image
        :param img: Image
        """
        img = img.resize((width, height))
        return img
    @staticmethod
    def scale ( img:Image.Image, factor)    -> Image.Image:
        """
        Scale image
        :param img: Image
        """
        img = img.resize((int(img.width * factor), int(img.height * factor)))
        return img
    @staticmethod
    def blur( img:Image.Image, pixel_size) -> Image.Image:
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
    @staticmethod
    def edge_detection( img:Image.Image) -> Image.Image:
        """
        Edge detection
        :param img: Image
        """
        img = img.convert('L')
        img = img.filter(ImageFilter.FIND_EDGES)
        return img
    @staticmethod
    def sovraimpose( img:Image.Image, img2:Image.Image) -> Image.Image:
        """
        Sovraimpose image
        :param img: Image
        """
        img = img.convert('RGBA')
        img2 = img2.convert('RGBA')
        img = Image.blend(img, img2, 0.5)
        return img
    # @staticmethod
    # def outline( img:Image.Image, outline:Image.Image, pixel_size) -> Image.Image:
    #     """
    #     follows the edges of the image in order to outline them with 1 pixel of contour
    #     :param img: Image
    #     """
    #     np_img = np.array(img)
    #     np_outline = np.array(outline)
    #     h,w,c = np_img.shape
    #     new_h = h // pixel_size
    #     new_w = w // pixel_size
    #     res = np.copy(np_img)
    #     outline_threshold = 180 # threshold for the outline, 0 is min and 255 is max
    #     outline_mask = np_outline > outline_threshold
    #     for i in range(new_h):
    #         for j in range(new_w):
    #             # get pixel value as mean of pixel_size x pixel_size square
    #             color:bool = outline_mask[i*pixel_size:(i+1)*pixel_size,j*pixel_size:(j+1)*pixel_size].any()
    #             # set pixel value for pixel_size x pixel_size square
    #             if color:
    #                 res[i*pixel_size:(i+1)*pixel_size,j*pixel_size:(j+1)*pixel_size,:] = 0
    #     outlined_img = Image.fromarray(res)
    #     return outlined_img
        @staticmethod
    def outline( img:Image.Image, outline:Image.Image, pixel_size) -> Image.Image:
        """
        follows the edges of the image in order to outline them with 1 pixel of contour
        :param img: Image
        """
        np_img = np.array(img)
        np_outline = np.array(outline)
        h,w,c = np_img.shape
        new_h = h // pixel_size
        new_w = w // pixel_size
        res = np.copy(np_img)
        outline_threshold = 180 # threshold for the outline, 0 is min and 255 is max
        outline_mask = np_outline > outline_threshold
        for i in range(new_h):
            for j in range(new_w):
                # get pixel value as mean of pixel_size x pixel_size square
                color:bool = outline_mask[i*pixel_size:(i+1)*pixel_size,j*pixel_size:(j+1)*pixel_size].any()
                # set pixel value for pixel_size x pixel_size square
                if color:
                    res[i*pixel_size:(i+1)*pixel_size,j*pixel_size:(j+1)*pixel_size,:] = 0
        outlined_img = Image.fromarray(res)
        return outlined_img
if __name__ == '__main__':
    # open image
    img = Image.open('img.png')
    edges = Pixie.edge_detection(img)
    edges.show()
    # resize image
    # show image
    pixellated = Pixie.pixellate(img, 10)
    pixellated.show()

    pixellated_edges = Pixie.edge_detection(pixellated)
    pixellated_edges.show()
    
    sovraimposed = Pixie.sovraimpose(pixellated, pixellated_edges)
    sovraimposed.show()
    
    edges_resized = Pixie.resize(edges, 1000, 1000)
    inverted = ImageOps.invert(edges_resized)
    pixellated_resized = Pixie.resize(pixellated, 1000, 1000)
    # sovraimposed_alt = Pixie.sovraimpose(edges_resized, pixellated_resized)
    # sovraimposed_alt.show()
    # blur = Pixie.blur(img, 20)
    # blur.show()
    Pixie.outline(pixellated, edges_resized, 10).show()