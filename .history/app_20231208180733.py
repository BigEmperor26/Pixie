# image library
from PIL import Image, ImageFilter, ImageOps
from PIL.ImageMorph import LutBuilder, MorphOp
import cv2
# cache
from functools import lru_cache
# TO DO resize to nearest positive multiple of pixel_size before pixellate and then resize back
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
  
    @staticmethod
    def outline( img:Image.Image, outline:Image.Image) -> Image.Image:
        """
        follows the edges of the image in order to outline them with 1 pixel of contour
        :param img: Image
        """
        np_img = np.array(img, dtype = np.uint8)
        np_outline = np.array(outline, dtype = np.uint8)
        res = np.copy(np_img)
        res[:,:,-1] -= np_outline
        
        outlined_img = Image.fromarray(res)
        return outlined_img
    @staticmethod
    def recolour( img:Image.Image, colors:int) -> Image.Image:
        """
        Recolour image
        :param img: Image
        """
        img = img.convert('P', palette=Image.ADAPTIVE, colors=colors)
        img = img.convert('RGBA')
        return img
    @staticmethod
    def recolour_palette( img:Image.Image, palette:list[tuple[int,int,int]], pixel_size) -> Image.Image:
        """
        Recolour image with custom palette of colors in RGB format
        :param img: Image
        """
        # pal:list = np.array(palette, dtype = np.uint8).tolist()
        img = img.convert('RGB')
        np_img = np.array(img)
        h,w,c = np_img.shape
        new_np_img = np.zeros((h,w,c),dtype = np.uint8)
        # loop through pixels each channel at the time

        for i in range(0,h-1, pixel_size):
            for j in range(0,w-1, pixel_size):
                # get pixel value as mean of pixel_size x pixel_size square
                pixel = Pixie.most_similar_colour(tuple(np_img[i,j,:]), palette)
                # set pixel value for pixel_size x pixel_size square
                new_np_img[i:i+pixel_size,j:j+pixel_size,:] = pixel
        return Image.fromarray(new_np_img)
    @staticmethod
    @lru_cache(maxsize=1024, typed=True)
    def most_similar_colour(colour:tuple[int,int,int], palette:list[tuple[int,int,int]]) -> tuple[int,int,int]:
        """
        Find the most similar colour in the palette
        :param colour: RGB colour
        """
        best = palette[0]
        # euclidean distance
        best_dist = np.linalg.norm(np.array(colour) - np.array(best))

        for c in palette:
            dist = np.linalg.norm(np.array(colour) - np.array(c))
            if dist < best_dist:
                best = c
                best_dist = dist
        return best

    @staticmethod
    def outline_pixels( img:Image.Image, outline:Image.Image, pixel_size) -> Image.Image:
        """
        follows the edges of the image in order to outline them with 1 pixel of contour
        :param img: Image
        """
        np_img = np.array(img)
        np_outline = np.array(outline)
        h,w,c = np_img.shape
        new_h = h // pixel_size
        new_w = w // pixel_size
        res = np.copy(np_img) # non clippare!!! aggiungo nero in base alla maschera
        # outline_threshold = 50 # threshold for the outline, 0 is min and 255 is max
        # outline_mask = np_outline > outline_threshold
        for i in range(new_h):
            for j in range(new_w):
                # get pixel value as mean of pixel_size x pixel_size square
                
                res[i*pixel_size:(i+1)*pixel_size,j*pixel_size:(j+1)*pixel_size,-1]  -= np_outline[i*pixel_size:(i+1)*pixel_size,j*pixel_size:(j+1)*pixel_size].max()
                # set pixel value for pixel_size x pixel_size square
                # if color:
                #     res[i*pixel_size:(i+1)*pixel_size,j*pixel_size:(j+1)*pixel_size,:] = 0
        outlined_img = Image.fromarray(res)
        return outlined_img
    @staticmethod
    def outline_edges( img:Image.Image) -> Image.Image:
        lb = LutBuilder(op_name='dilation')
        dil = MorphOp(lb.build_lut())
        lb = LutBuilder(op_name='erosion')
        ero = MorphOp(lb.build_lut())
        _,img = dil.apply(img)
        _,img = ero.apply(img)
        return img
    @staticmethod
    def pixellate_resize( img:Image.Image, pixel_size) -> Image.Image:
        """
        Pixellate image
        :param img: Image
        """
        np_img = np.array(img)
        h,w,c = np_img.shape
        
        new_np_img = np.zeros((h*pixel_size,w*pixel_size,c),dtype = np.uint8)
        # loop through pixels each channel at the time
        for c in range(np_img.shape[-1]):
            for i in range(h):
                for j in range(w):
                    # get pixel value as mean of pixel_size x pixel_size square
                    pixel = np_img[i:i+1,j:j+1,c]
                    # set pixel value for pixel_size x pixel_size square
                    new_np_img[i*pixel_size:(i+1)*pixel_size,j*pixel_size:(j+1)*pixel_size,c] = pixel
        
        new_img = Image.fromarray(new_np_img) 
        return new_img
if __name__ == '__main__':
    # open image
    img = Image.open('img.png')
    # img = Image.open('luffy.png')
    # img = Image.open('zoro.webp')
    # img = Image.open('sanji.webp')
    
    # pixellated = Pixie.pixellate(img_rc, 10)
    # pixellated.show()
    img_rc = Pixie.recolour(img, 32)
    
    
    small  = Pixie.scale(img_rc, 0.1)
    small = small.filter(ImageFilter.EDGE_ENHANCE)
    small.show()
    
    pix = Pixie.pixellate_resize(small, 5)
    pix.show()
    
    cv_filter = cv2.filter2D(np.array(small), -1, np.array([[-1,-1,-1], [-1,5,-1], [-1,-1,-1]], dtype=np.int8))
    import pdb; pdb.set_trace()
    Image.fromarray(cv_filter).show()