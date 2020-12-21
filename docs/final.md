---
layout: default
title:  Final Report
---

## Video (this is old video, we need to update... delete this when updated)

<iframe width="560" height="315" src="https://www.youtube.com/embed/brrMn67sN6M" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Project Summary

Our goal for this project went through many iterations, trying to figure out a project that was feasible and would pique our interest. We had some crazy ideas before (agent battle royale), but settled on prediction of each pixel of the player perspective. This includes labeling of Minecraft structures including trees, house, and lake as classes. A combination of given Malmo functions would be able to determine block/entity identity, but in order to classify structures and evaluate its accuracy, we needed to use machine learning algorithms.

An obstacle was using Malmo's functionality to get the location of block/entity, determine whether or not it was in player's view, figure the type of block/entity, and the structure that it was apart of. We had a lot of information to use to decipher simply reading the blocks on the player's screen. Part of our solution involved generating a color map and matching the color ID of the screen to blocks/entities in Minecraft.

Part of our list of prioirities included increasing efficiency of our model which was evaluated using the metrics explained in the Evaluation section. Our model took multiple hours to run before due to the sheer size of data we collected, so we 




## Approaches



## Evaluation



## References

Checkpoint usage for running our algorithm:
https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_a_general_checkpoint.html
