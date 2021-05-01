# DataViz_CT_CCR


Utilities to produce data vizualisation figures on nifti file (modality **computerized tomography** CT scan) along 3D slices of **Colorectal cancer** (with corresponding binary tumor mask) on
126 patients.

The dataset can be used for semantic/instance segmentation and object detection as well.


## Dataset

This dataset was initialy used at a [Medical Segmentation Decathlon](http://medicaldecathlon.com/) for segmentation task.

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

Project repository should be organized as below with image and corresponding mask (must have the same name) in imagesTr and labelsTr folder respectively.

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

## Data visualization on medical images


Medical images such as MRI or CT scan are 3D objects often difficult to visualize in publications. One solution is to create
a 3D representation with all 2D slices. Another solution, adressed here, is to plot selected 2D slices among all image stack
and their corresponding tumor masks.

First, we need verify if there is no problem in the dataset :

- Do all images/masks are in the same size?
- Do all images have a corresponding mask?
- Are masks binary ? (0 : pixel do not contained tumor, 1 : pixel containing tumor)


(Here we do not adressed issues about image preprocessing including intensity normalization, noise and contrast...).


The job is quite easy on this dataset as all images already have consistent 512/512 pixels size with corresponding binary mask. But do we have the same number
of images per patient? And do we have equal number of image/mask with and without tumor?

Let's see that. We just need to quantify the number of completely black masks (= no tumors). For later use, we also created a function returning the index
of images/mask with tumors.

Then we can collect number of slices with and without tumors for each patient into a dataframe and plot the data.

![alt text](https://github.com/hbiom/DataViz_CT_CCR//blob/main/img/slices_graph.png?raw=true)


As we see of these graphs, most patients have around 100 slices, but only 10% of total images actually contain a tumor. I guess radiologists have to scan the entire
abdominal region to find the tumor, resulting in this low ratio. That would be a problem to train a deep learning algorithm for segmentation/clasification, as the number
of positive/negative class in this case should be similar.

For our visualization task, this is just a fact for us to notice, not affecting the results.


To have a global idea of the aspect of 3D object, We first need to visualize individual 2D images from the first slice to the last one with equidistant
intermediary slices (we set the max number of images displayed by 18). We used the function *plot_image* on patient **0050_Colon**.

We obtain the images below:

![alt text](https://github.com/hbiom/DataViz_CT_CCR//blob/main/img/plot_image.png?raw=true)


We can see the scan begins below the thigh and up to the lungs covering all abdominal region. The colorectal tumor is somewere between this slices. We can spot it
by ploting the correspong tumor mask. To do so we can used the argument *dislay_mode ='mask'* of our custom plot_image function to see tumor.

We can see the entire tumor shape by just overlapping the mask on the images:

![alt text](https://github.com/hbiom/DataViz_CT_CCR//blob/main/img/plot_image_tumors.png?raw=true)


Okay, the tumor seem to appear from around slice 57, and finish around slice 89. As this point, we know where the tumor is, but we might want to have a better
look on it. We can set the argument of plot_image show_tumor_only = True to only display images containing tumors from the first slice to the last one with
equidistant intermediary slices. This way we can see the global shape of the tumor along all the slices.

![alt text](https://github.com/hbiom/DataViz_CT_CCR//blob/main/img/plot_image_mask_show_tumor_only.png?raw=true)


We might want to spot the tumor in another way. For instance, we can see the same slices and visualize the countour of the tumor mask, overlapping it on the images:

![alt text](https://github.com/hbiom/DataViz_CT_CCR//blob/main/img/plot_image_contour_show_tumor_only.png?raw=true)

We can also retrive tumor's mask bounding box coordinates and plot it on corresponding images.

![alt text](https://github.com/hbiom/DataViz_CT_CCR//blob/main/img/plot_image_bbounding_show_tumor_only.png?raw=true)

To finish, we might want to focus on one tumor slice, most likely the one where the tumor is the biggest. To spot it, we just need to find the the mask with
the most positive events. We can then plot the images with the bounding box, with the corresponding cropped images around the tumor and finally just the tumor.

*functions to retrieve mask coordinate and cropped image come from this repository [Here](https://github.com/guillaumefrd/brain-tumor-mri-dataset)*


We obtain the image below:

![alt text](https://github.com/hbiom/DataViz_CT_CCR//blob/main/img/tumor_all.png?raw=true)


## Optional


Now we can combine all graphs into a publication-like figure:


![alt text](https://github.com/hbiom/DataViz_CT_CCR//blob/main/img/bilan.png?raw=true)


**Figure 1:** Proportion of number of slices by patient (**A**) and total distribution of slices containing tumors or not from 126 patients with colorectal cancer.
Exemple of slices of tumors with contour on one patient (**B**). Focus on the slice with the largest tumor slice (**C**) on patient represented in B.

## Final note

There is much more we can do to visualize medical images that is not covered here, like 3D reconstitution and image preprocessing, as well as the development of advanced
techniques with amazing library.

Still, basic visualization of the dataset is a good start before implementing complex machine learning solutions.


Thanks for reading !


Feedback are welcome and will be appreciated.



