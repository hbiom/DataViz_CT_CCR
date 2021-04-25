# DataViz_CT_CCR


Utilities to produce data vizualisation figures on nifti file (modality CT scan) along 3D slices of Colorectal cancer (with corresponding tumor mask) on
126 patients.

The dataset can be used for visualization, semantic/instance segmentation and object detection.


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


![alt text](https://github.com/hbiom/DataViz_CT_CCR//blob/main/img/slices_graph.png?raw=true)
![alt text](https://github.com/hbiom/DataViz_CT_CCR//blob/main/img/plot_image_tumors.png?raw=true)
![alt text](https://github.com/hbiom/DataViz_CT_CCR//blob/main/img/plot_image.png?raw=true)
![alt text](https://github.com/hbiom/DataViz_CT_CCR//blob/main/img/plot_image_contour_show_tumor_only.png?raw=true)
![alt text](https://github.com/hbiom/DataViz_CT_CCR//blob/main/img/plot_image_mask_show_tumor_only.png?raw=true)
![alt text](https://github.com/hbiom/DataViz_CT_CCR//blob/main/img/tumor_all.png?raw=true)
