# image library
from PIL import Image, ImageFilter, ImageOps\
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
if __name__ == '__main__':
    # open image
    # img = Image.open('img.png')
    img = Image.open('zoro.webp')
    # img_rec = Pixie.recolour(img, 32)
    # img_rec.show()
    # CONVERT TO RGBA
    edges = Pixie.edge_detection(img)
    # edges.show()
    # resize image
    # show image
    pixellated = Pixie.pixellate(img, 15)
    pixellated.show()

    pixellated_edges = Pixie.edge_detection(pixellated)
    # pixellated_edges.show()
    
    # sovraimposed = Pixie.sovraimpose(pixellated, pixellated_edges)
    # sovraimposed.show()
    
    # edges_resized = Pixie.resize(edges, 1000, 1000)
    # inverted = ImageOps.invert(edges_resized)
    # pixellated_resized = Pixie.resize(pixellated, 1000, 1000)
    # sovraimposed_alt = Pixie.sovraimpose(edges_resized, pixellated_resized)
    # sovraimposed_alt.show()
    # blur = Pixie.blur(img, 20)
    # blur.show()
    recoloured = Pixie.recolour(img, 32)
    # recoloured.show()
    pixellated_recoloured = Pixie.pixellate(recoloured,10)
    pixellated_recoloured.show()

    
    custom_palette = [(0,0,0),(128,128,128), (255,255,255), 
                      
                         (128,0,0), (255,0,0), 
                      (0,255,0), (0,128,0), 
                      (0,0,255), (0,0,128), 
                      
                      (128,128,0), (255,255,0),
                      (128,0,128), (255,0,255),
                      (0,128,128), (0,255,255),
                      
                    #   (128,128,128), (255,255,255),
                      
                      ]
    # custom_palette = [
    #   [140, 143, 174],
    #   [88, 69, 99],
    #   [62, 33, 55],
    #   [154, 99, 72],
    #   [215, 155, 125],
    #   [245, 237, 186],
    #   [192, 199, 65],
    #   [100, 125, 52],
    #   [228, 148, 58],
    #   [157, 48, 59],
    #   [210, 100, 113],
    #   [112, 55, 127],
    #   [126, 196, 193],
    #   [52, 133, 157],
    #   [23, 67, 75],
    #   [31, 14, 28],
    # ]
    res = tuple(tuple(sub) for sub in custom_palette)
    recoloured_custom = Pixie.recolour_palette(pixellated, res, pixel_size=10)
    recoloured_custom.show()

    Pixie.outline_pixels(pixellated, edges,pixel_size=5).show()
    # Pixie.outline(pixellated_recoloured, pixellated_edges).show()
    
    