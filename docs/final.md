---
layout: default
title:  Final Report
---

## Video (this is old video, we need to update... delete this when updated)

<iframe width="560" height="315" src="https://www.youtube.com/embed/brrMn67sN6M" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Project Summary

Our goal for this project went through many iterations, we began by trying to figure out a project that was feasible while also piquing our interests. We had some project ideas before such as agent battle royale, but ultimately settled on a image classification problem known as semantic segmentation. Semantic segmentation involves classifying each  each pixel of an image to some class e.g. water, sky, dirt(figure 1 maybe the video,ground truth,predictions image).

A combination of Malmo functions made it possible for us to determine what block/entities were on the players screen, however, this does not apply to normal minecraft. In normal minecraft the only way to determine the location and type of blocks/entities that are contained within the players perspective is by having someone who is qualified manually look and decide, however, in malmo we are able to generate color maps which have corrsesponding colors for each block/entity. In order to semanticaly segment normal minecraft it was necessary apply machine learning algorithms.


<div style="text-align:center"><img src="./images/colormap_2186.png" width="400"/> </div>
<div style="text-align:center"><img src="./images/video_2186.png" width="400"/> </div>


## Approaches
Before we could apply any machine learning algorithms to aid us in our semantic segmentation task we needed to create the ground truth images for our training and test set.
this introduced The main obstactle of the project, malmos colour map producer. The color maps that malmo returns although visually identify each entity/block with a unique color in practice this is not the case, for each block/entity there was tens of thousands of very similar looking although unique colors which identified each block/entity (figure 2 the fucked up image with a lot of white). We had to find a way to compare all these similar colors and group them with eachother in order to create the ground truth images for our semantic segmentation algorithms. To solve this we found the most dominant color for each class, then converted every RGB image to a CIELAB color space and then compared them each color to one another using the CIEDE2000 formula to find which were the most similar to their respective dominant colors. In doing so we had 132 different classes each with their own unique color, this let us convert every rgb image into a greyscale image containing numbers from 0-132(figure 3 a normal rgb mask).
For our semantic segmentation problem we used a neural network following the DeepLabv3 architechture pretrained on resnet 101 as our model of choice.



## Evaluation

### Elbow Method for K-Means Evaluation

For part of our K-means evaluation, we wanted to choose the optimal value of k. There were over 100 different colors and possible clusters, so we wanted an ideal k for that represented the sum of our images. We chose the elbow method which determined the optimal value for k based on the sum of squared distances (SSE) between data points and the cluster centroids. We first evaluated using the elbow method on one image with k=40 and then proceeded to test this multiple times to a numerous sample of images:



Elbow Method on one image:

<div style="text-align:center"><img src="./images/kmeans/elbow0.png" width="400"/> </div>


Elbow Method on a sample of images:


<div style="text-align:center"><img src="./images/kmeans/elbow_all_k40.png" width="400"/> </div>


Looking at the example graph, it would seem k=2 would be a clear choice for optimality, however we chose not to go with k value because we believed there may have been too much bias of our player perspective from looking at the blue sky or gray cobblestone floor. We chose the k value of 8 as from the sum of our tests, it seemed to be the next most optimal k value.

We applied k=2 and k=8 to our images to see the difference between these values. The results are shown below:

Original:


<div style="text-align:center"><img src="./images/kmeans/img0_org.png" width="400"/> </div>


k=2:


<div style="text-align:center"><img src="./images/kmeans/img0_k2.png" width="400"/> </div>


k=8:


<div style="text-align:center"><img src="./images/kmeans/img0_k8.png" width="400"/> </div>




### Intersection Over Union 

Intersection over Union (IoU) is a metric designed for evaluation of object detection, which was the perfect metric to use in our model. For this metric, two bounds are used: the ground truth bounding boxes and the prediction bounding boxes from the model. The IoU is then calculated by divding the area of overlap and the area of union between the bounding boxes. Through 51 epochs, we used this metric and to evaluate our model. the graphs show the IoU values for the training and testing over these epochs.


Training IoU:


<div style="text-align:center"><img src="./images/dataplots/ioutr.png" width="400"/> </div>


Testing IoU:


<div style="text-align:center"><img src="./images/dataplots/ioute.png" width="400"/> </div>


## References

https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_a_general_checkpoint.html

https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/#:~:text=What%20is%20Intersection%20over%20Union,the%20popular%20PASCAL%20VOC%20challenge.

https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html

https://en.wikipedia.org/wiki/CIELAB_color_space

https://github.com/chenxi116/DeepLabv3.pytorch

https://arxiv.org/pdf/1606.00915.pdf

https://neptune.ai/blog/image-segmentation-in-2020

https://python-colormath.readthedocs.io/en/latest/

https://pytorch.org/tutorials/recipes/recipes/custom_dataset_transforms_loader.html
