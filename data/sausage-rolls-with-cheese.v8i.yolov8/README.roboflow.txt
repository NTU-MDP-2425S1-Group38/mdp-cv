
sausage-rolls-with-cheese - v8 2024-08-24 4:03pm
==============================

This dataset was exported via roboflow.com on August 24, 2024 at 4:05 PM GMT

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

The dataset includes 1403 images.
Visual-target-cards are annotated in YOLOv8 format.

The following pre-processing was applied to each image:
* Resize to 640x640 (Fit (black edges))

The following augmentation was applied to create 3 versions of each source image:
* Random rotation of between -15 and +15 degrees
* Random shear of between -14° to +14° horizontally and -14° to +14° vertically
* Random brigthness adjustment of between -25 and +25 percent
* Random exposure adjustment of between -19 and +19 percent
* Random Gaussian blur of between 0 and 1.5 pixels
* Salt and pepper noise was applied to 2.28 percent of pixels

The following transformations were applied to the bounding boxes of each image:
* Salt and pepper noise was applied to 0.04 percent of pixels


