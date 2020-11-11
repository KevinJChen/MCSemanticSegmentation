---
layout: default
title:  Status
---

Summary:


Approach:
Our approach can be broken into a few steps. The first step was data gathering which was a little more complicated than it
may seem. In order for us to train data, we needed to know the all the blocks and entities on the player's screen as well as
the location and its distance from the player. We achieved this by scanning the area to know each available type of block,
receiving a 3D array and sifting through each element to determine the surface visible to the player. After the data is obtained,
it is fed into the trainig algorithm where it will be trained across numerous datasets to make it as accurate as possible. A
k-means algorithm will also be along the side to give us an approximate evaluation of the performance of our algorithm which we
can use to compare the results and accuracy of the labeling.

Evaluation:


IOU Performance


Remaining Goals and Challenges:
We are attempting to train the data in the person's view to label the different structures including tree and building. This is
achieved by adding a deep learning algorithm and a reinforcement learning algorithm which we are currently sifting through 
the details for. The algorithm ideas and implementation were the re sult of researchhing reading multiple learning algorithms that
have been implemented into real life semantic segmentations. These algorithms are often much more detailed and account for a lot
more than we may need for Minecraft because ultimately, there are more details in the real world than Minecraft. We will end by 
the evaluation where a quick k-means algorithm will be used to evaluate the performance of the implemented learning algorithms.

Resources Used:




