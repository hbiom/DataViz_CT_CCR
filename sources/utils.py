
import os
import pandas as pd

import imageio
import nibabel as nib
import scipy.ndimage as ndi
import cv2
import SimpleITK as sitk
from skimage import io
from skimage.measure import find_contours

import math
import numpy as np
import cv2
import SimpleITK as sitk
from skimage import io
from skimage.measure import find_contours

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt




def get_bounding_box(mask, crop_margin=0):
    """
    Return the bounding box of a mask image.
    slightly modify from https://github.com/guillaumefrd/brain-tumor-mri-dataset/blob/master/data_visualization.ipynb
    """
    xmin, ymin, xmax, ymax = 0, 0, 0, 0

    for row in range(mask.shape[0]):
        if mask[row, :].max() != 0:
            ymin = row + crop_margin
            break

    for row in range(mask.shape[0] - 1, -1, -1):
        if mask[row, :].max() != 0:
            ymax = row + crop_margin
            break

    for col in range(mask.shape[1]):
        if mask[:, col].max() != 0:
            xmin = col + crop_margin
            break

    for col in range(mask.shape[1] - 1, -1, -1):
        if mask[:, col].max() != 0:
            xmax = col + crop_margin
            break

    return xmin, ymin, xmax, ymax


def crop_to_bbox(image, bbox, crop_margin=0):
    """
    Crop an image to the bounding by forcing a squared image as output.
    from https://github.com/guillaumefrd/brain-tumor-mri-dataset/blob/master/data_visualization.ipynb
    """
    x1, y1, x2, y2 =  bbox

    # force a squared image
    max_width_height = np.maximum(y2 - y1, x2 - x1)
    y2 = y1 + max_width_height
    x2 = x1 + max_width_height

    # in case coordinates are out of image boundaries
    y1 = np.maximum(y1 - crop_margin, 0)
    y2 = np.minimum(y2 + crop_margin, image.shape[0])
    x1 = np.maximum(x1 - crop_margin, 0)
    x2 = np.minimum(x2 + crop_margin, image.shape[1])

    return image[y1:y2, x1:x2]


def plot_bbox_image(image, mask, crop_margin=0, zooming=False):
  '''
    Plot slices with bounding boxe containing the tumor
    masks is binary (0 : pixel do not contained tumor , 1 : pixel containing tumor)
    image and mask are 2D array with same dimensions
  '''

  if len(mask.shape) != 2:
    raise ValueError("only accept one array of 2D dimension")

  xmin, ymin, xmax, ymax = get_bounding_box(mask, crop_margin)

  plt.imshow(image, cmap='gray')
  plt.plot([xmin, xmax], [ymin, ymin], color='red')
  plt.plot([xmax, xmax], [ymin, ymax], color='red')
  plt.plot([xmin, xmin], [ymin, ymax], color='red')
  plt.plot([xmin, xmax], [ymax, ymax], color='red')

  if zooming:
    plt.plot([xmax, 511], [ymax, 511], color='red')
    plt.plot([xmax, 511], [ymin, 0], color='red')
