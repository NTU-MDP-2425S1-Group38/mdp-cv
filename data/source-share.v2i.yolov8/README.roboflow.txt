
Instance Segmentation - v2 2024-09-12 3:54pm
==============================

This dataset was exported via roboflow.com on September 12, 2024 at 3:57 PM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 9660 images.
Sym are annotated in YOLOv8 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Fit (black edges))
* Auto-contrast via contrast stretching

The following augmentation was applied to create 3 versions of each source image:
* Random rotation of between -5 and +5 degrees
* Random shear of between -9° to +9° horizontally and -9° to +9° vertically
* Random brigthness adjustment of between -15 and +15 percent
* Random exposure adjustment of between -15 and +15 percent
* Random Gaussian blur of between 0 and 2.5 pixels
* Salt and pepper noise was applied to 1.96 percent of pixels

The following transformations were applied to the bounding boxes of each image:
* Salt and pepper noise was applied to 0.28 percent of pixels


