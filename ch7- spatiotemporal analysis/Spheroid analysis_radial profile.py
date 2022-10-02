# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 16:36:00 2021

@author: nilou
"""

import sys
sys.path.append('C:/Users/nilou/')

import os
import cv2 as cv
import skimage
import glob
import csv
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib 
import napari
import czifile
import distancemap
import matplotlib as mpl
from matplotlib import pyplot as plt
from scipy import ndimage, misc
import imgfileutils1_without_well_info as imf
import segmentation_tools as sgt
from skimage import io, color, measure , segmentation
from skimage.measure import label, regionprops, regionprops_table
import czifile as zis
from aicsimageio import AICSImage, imread
from aicsimageio.writers import OmeTiffWriter
from skimage.filters import threshold_otsu
from scipy import ndimage
from scipy.ndimage.morphology import distance_transform_edt
from skimage.morphology import erosion, dilation, opening, closing, white_tophat, disk, black_tophat, skeletonize, convex_hull_image
import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm


# 1: reading and loading the image from directory ######################################

PATH_in = 'G:/2021/20210820/live  spheroid diffusion- MCF7- t10 - ucnpz@Dox.tif'
Path_in_mask = 'G:/2021/20210820/masks/MCF7-dox.tif'
name = os.path.split(PATH_in)[-1]
PATH_out = 'G:/2021/20210820/'     #### specify the path to save the images
pixel_to_um = 0.35                                             #### specify scale of the image
imG = AICSImage(PATH_in)
imGmask = AICSImage(Path_in_mask)
# img = czifile.imread(PATH_in)

shape = np.shape(imG)
print(shape)
# subset = img [0,0,:,0,0,:,:,:]
# shape1 = np.shape(img)
# print(subset.shape)


chmask = imGmask.get_image_data("YX", S=1, T=0 , Z=0, C=0)  # returns 3D ZYX numpy array
ch0 = imG.get_image_data("YX",S=1, T=0 , Z=0, C=4) 
Channels = imG.channel_names
shape = np.shape(chmask)
print(shape)

# chmask = np.max(chmask) - chmask
# thresh = threshold_otsu(chmask)
# binary = chmask > thresh * 0.5
# for i in range(3):
#     binary = ndimage.binary_closing(binary)
#     binary = ndimage.binary_fill_holes(binary)
    

# clearimage = segmentation.clear_border(binary)
dist = ndimage.distance_transform_edt(chmask)

bin_size = 5
d_max = int(np.max(dist)/bin_size)
print(d_max)

# 2: Napari ############################################################################

# viewer = napari.view_image(subset)

#%%############################################################################################
### Define Segmentation Options - 1 ###

# define channel and size filter for objects
chindex = 2  # channel containing the objects, e.g. the nuclei in DAPI channel
minsize = 5000000  # minimum object size [pixel]
# maxsize = 10000000000000000  # maximum object size [pixel]


# set number of Scenes for testing
#SizeS = 1

###############################################################################################
# get the metadata from the czi file
# md = imf.get_metadata_czi(PATH_in, dim2none=False)

###############################################################################################

# cols = ['d', 'I', 'std', 'C']
# objects = pd.DataFrame(columns=cols)
# set image counter to zero and create empty dataframe
image_counter = 0
results = pd.DataFrame()



# 3: Creating distance contours #########################################################


d = np.zeros(d_max)
I = np.zeros(d_max)
std = np.zeros(d_max)
chi = np.zeros(d_max)

#%%

for c in (range(1)): 
    # image = imG.get_image_data("YX", S=1, T=0 , Z=0, C=2)
    # thresh = threshold_otsu(image)
    # binary = image > thresh
    # for i in range(4):
    #         binary = ndimage.binary_dilation(binary)
    #         binary = ndimage.binary_fill_holes(binary)

    # clearimage = segmentation.clear_border(binary)
    # dist = ndimage.distance_transform_edt(clearimage)
    ch = imG.get_image_data("YX", S=1, T=0 , Z=0, C=c)
    
    for i in (range(d_max)):
    
        mask = np.logical_and( i * bin_size < dist , dist < (i+1) * bin_size)
        profile = ch [mask]
        I[i] = np.mean(profile)
        std[i] = np.std(profile)
        d[i] = 1 + i* bin_size 
        chi[i] = c
       
    results1 = np.stack((d * pixel_to_um, I, std, chi), axis = -1)
    results = results.append(pd.DataFrame(results1), ignore_index=True)
     
results.columns =['d', 'I', 'std', 'C']        
print(results1.shape, results.shape)
# pd.DataFrame(results1).to_csv(PATH_out + name + '_distance_profiles.csv', index=False)
results.to_csv(PATH_out + name + '_distance_profiles_ch.csv', index=False)

#%%
# 3:Plotting intensity profile ########################################################

# plt.
cmap = plt.get_cmap('viridis', (shape[1]))
# color = iter(cm.viridis(np.linspace(0,1,(md['SizeC']))))
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
            
for c in (range(shape[1])): 
    
    subset = results[results.C == c]
    # plt.plot(np.max(subset['d']) - subset['d'], subset['I']/np.max(subset['I']), color=next(color)) 
    # plt.plot(np.max(subset['d']) - subset['d'], subset['I'], c=cmap(c))
    # plt.fill_between(np.max(subset['d']) - subset['d'], (subset['I'] - subset['std']), (subset['I'] + subset['std']),
    #                   color=cmap(c), alpha=0.2) 
    plt.plot(subset['d'], subset['I'], c=cmap(c))
    plt.fill_between( subset['d'], (subset['I'] - subset['std']), (subset['I'] + subset['std']),
                      color=cmap(c), alpha=0.2) 
    # plt.fill_between(np.max(subset['d']) - subset['d'], 
    #                   1.1*subset['I']/np.max(subset['I']),
    #                   0.85*subset['I']/np.max(subset['I']),
    #                   c=cmap(c), alpha=0.2)
plt.xlabel('Distance from the spheroid edge (microns)')
plt.ylabel('Normalized Intensity (A.U,)')

# plt.colorbar()

# plt.fill_between(d/2.5, (intensity - std)/10, (intensity + std)/10,
#                       color='pink', alpha=0.2)    

plt.show()
# 
       
# 5: Writing Image #####################################################################




