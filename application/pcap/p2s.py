import imageio
import scipy.ndimage
import numpy as np
import requests
import matplotlib.pyplot as plt

########################################################################################################################
#This class is birthed from this notebook found at the user aloksonker1952@github.com's page. https://github.com/aloksonker1952/Pic_2_Sketch/blob/master/Pic_2_Sketch.ipynb. I call it the p2s class because it is the comparison against the GAN;  hope to use it and the Gan to create new datasets of images and sketches from users. 

#######################################################################################################################
class p2s():
    def __init__(self, image):
        self.image = image

    #def getImage(self, img):
    #    return dp.image = self.img

    def readImage(img):
        source_img = imageio.imread(img)
        return source_img

    def grayscaleing(rgb):
        return np.dot(rgb[...,:3],[0.299,0.587,0.114])
      
    def showGrayscale(source_img):  
        gryscl_img = grayscaleing(source_img)
        inv_img = (255 - gryscl_img)
        return plt.imshow(inv_img)

    def showBlurry(_img):
        gryscl_img = grayscaleing(_img)
        inv_img = (255 - gryscl_img)
        blurred_img = scipy.ndimage.filters.gaussian_filter(inv_img, sigma=5)
        return plt.imshow(blurred_img)

    def dodging(blur_img,gryscl_img):
        resultant_dodge=blur_img*255/(255-gryscl_img)
        resultant_dodge[resultant_dodge>255]=255
        resultant_dodge[gryscl_img==255]=255
        return resultant_dodge.astype('uint8')


    def showSketch():
        gryscl_img = grayscaleing(source_img)
        inv_img = (255 - gryscl_img)
        blurred_img = scipy.ndimage.filters.gaussian_filter(inv_img, sigma=5)
        target_img = dodging(blurred_img, gryscl_img)
        return plt.imshow(target_img, cmap='gray')


