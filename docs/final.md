---
layout: default
title:  Final Report
---

## Video (this is old video, we need to update... delete this when updated)

<iframe width="560" height="315" src="https://www.youtube.com/embed/brrMn67sN6M" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Project Summary

Our goal for this project went through many iterations, trying to figure out a project that was feasible and would pique our interest. We had some crazy ideas before (agent battle royale), but settled on prediction of each pixel of the player perspective. This includes labeling of Minecraft structures including trees, house, and lake as classes. A combination of given Malmo functions would be able to determine block/entity identity, but in order to classify structures and evaluate its accuracy, we needed to use machine learning algorithms.

An obstacle was using Malmo's functionality to get the location of block/entity, determine whether or not it was in player's view, figure the type of block/entity, and the structure that it was apart of. We had a lot of information to use to decipher simply reading the blocks on the player's screen. Part of our solution involved generating a color map and matching the color ID of the screen to blocks/entities in Minecraft. An example of a generated color map is seen below:


<div style="text-align:center"><img src="./images/colormap_2186.png" width="400"/> </div>
<div style="text-align:center"><img src="./images/video_2186.png" width="400"/> </div>


## Approaches



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


<div style="text-align:center"><img src="./images/kmeans/ioute.png" width="400"/> </div>


## References

https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_a_general_checkpoint.html

https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/#:~:text=What%20is%20Intersection%20over%20Union,the%20popular%20PASCAL%20VOC%20challenge.

https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html
