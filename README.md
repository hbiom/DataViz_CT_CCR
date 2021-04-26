# DataViz_CT_CCR


Utilities to produce data vizualisation figures on nifti file (modality CT scan) along 3D slices of Colorectal cancer (with corresponding binary tumor mask) on
126 patients.

The dataset can be used for semantic/instance segmentation and object detectionas as well.


## Dataset

This dataset was initialy used for a [Medical Segmentation Decathlon](http://medicaldecathlon.com/) for segmentation task.

More information and link to dowload this dataset can be found [Here](https://drive.google.com/drive/folders/1HqEgzS8BV2c7xYNrZdEAnrHk7osJJ--2)


## Requirements

```
- imageio==2.9.0
- matplotlib==3.3.3
- nibabel==3.2.1
- numpy==1.19.5
- opencv-python==4.5.1.48
- openpyxl==3.0.5
- pandas==1.2.0
- scikit-image==0.18.1
- scipy==1.6.2
- seaborn==0.11.1
- SimpleITK==2.0.2
```


## Repository

Projet repository should be organised as below with image and corresponding mask (must have the same name) in imagesTR and labels folder respectively.

```
CT_CCR
│
│   CT_Coloreact_Viz_3D.ipynb
│   README.md
│   CCR_slices.csv
│   requirement.txt
│
│───sources
│    utils.py
│
│───Task10_Colon
│   │
│   │dataset.json
│   │
│   └────imagesTr
│   │
│   └────labelsTr
│
│───img

```



Medical images such as MRI or CT scan are 3D object often difficult to visualize in publication. One solution is to creates
3D representation with all 2D slices. Another solution describe adressed here, is to plot selected 2D slices along all images stack
and corresponding tumors.

First, we need if there no problem in the dataset including :

- Do all images/masks are in the same size ?
- Do all images have corresponding mask ?
- Are mask binary ? (0 : pixel do not contained tumor , 1 : pixel containing tumor)


(Here we do not adressed issues about image preprocessing including intensity normalisation, noise and contrast ...).


The job is quite easy on this dataset as all images are 512/512 pixels size with corresponding binary mask. But do we have the same number of images per
patients ? And do each patient have equal number of image/mask with and without tumor ?

Lets see that, We just need to quantify the number of mask completely black (= no tumors). For futher purposed, we also create a function returning the index
of images/mask with tumors.

![alt text](https://github.com/hbiom/DataViz_CT_CCR//blob/main/img/slices_graph.png?raw=true)


As we see of these graph, most of patient have around 100 slices, but only 10% of total images actually contain a tumor. I guess radiologist have to scan the entire
abdominal region to find the tumor resulting in this low number. That would be a problem to train a deep learning algorithm for segmentation/clasification as the number
of positive/negative class should be similar.

In ours visualization task, this is just a fact for us to notice.


To have a global idea of the aspect of 3D object, We first need to visualize individual 2D images from the first slice to the last one with equidistant
intermediary slices (We set the max number of images displayed by 18). we used the function plot_image on patient 0050_Colon.

We obtain the images below :

![alt text](https://github.com/hbiom/DataViz_CT_CCR//blob/main/img/plot_image.png?raw=true)


We can see the scan beging below the thigh and up to the lungs covering all abdominal region. The colorectal tumor is somewere between this slices. We can spot it
by ploting the correspong tumor mask. To do so we can used the argument dislay_mode ='mask' of our custom plot_image function to see tumor.

We can see the entire tumor shape by just overlapping the mask on the images :

![alt text](https://github.com/hbiom/DataViz_CT_CCR//blob/main/img/plot_image_tumors.png?raw=true)


Okay, the tumor seem to be appeard around slices 57 and finish slices 89. As this point, we know where the tumor is, but we migth want to have a better
look on it. We can set the argument of plot_image show_tumor_only = True to only display images containing tumors from the first slice to the last one with equidistant
intermediary slices. This way we can see the global shape of the tumor along all the slices.

![alt text](https://github.com/hbiom/DataViz_CT_CCR//blob/main/img/plot_image_mask_show_tumor_only.png?raw=true)


We migth want to spot the tumor other way. for instance, We can see the extract and visualize the countour of the tumor mask and overlapping it on the images :

![alt text](https://github.com/hbiom/DataViz_CT_CCR//blob/main/img/plot_image_contour_show_tumor_only.png?raw=true)

Lasty, we can retrive bounding box coordinates with the mask and plot it on corresponding images.

![alt text](https://github.com/hbiom/DataViz_CT_CCR//blob/main/img/plot_image_bbounding_show_tumor_only.png?raw=true)


To finish, we migth want to focus on one tumor slice, most likely the one where the tumors is the biggest. To spot it, we just need to find the the mask with
the most positive events. We can then plot the images with the bounding box, with the corresponding cropped images around the tumor and finally just the tumors.
We obtain the image below :

![alt text](https://github.com/hbiom/DataViz_CT_CCR//blob/main/img/tumor_all.png?raw=true)


There is much more we can do to visualize medical images not covered here like 3D reconstitution and image preprocessing, as well as the development of advanced
techniques and amazing library.

Still, visualization of the dataset a good start before implementing complex machine learning solutions.


Thanks for reading!


Feeback are welcome and error signaling will be appreciated.



