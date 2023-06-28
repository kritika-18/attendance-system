
# Automated Attendance System Using Face Recognition

This project is used to mark attendances of the students in schools, colleges and universities just by taking the pictures of the students.

The face detection and face recogniton is done by Haar Cascade and LBPH algorithms respectively.

**HAAR CASCADE ALGORITHM**

Haar cascade is an algorithm that can detect objects in images, irrespective of their scale in image and location. This algorithm is not so complex and can run in real-time. We can train a haar-cascade detector to detect various objects like cars, bikes, buildings, fruits, etc. The algorithm can be explained in four stages:

1. Calculating Haar Features
A Haar feature is calculations performed on adjacent rectangular regions at a specific location in a detection window. The calculation involves summing the pixel intensities in each region and calculating the differences between the sums. 
These features can be difficult to determine for a large image. This is where integral images come into play because the number of operations is reduced using the integral image.

2. Creating Integral Images
Without going into too much of the mathematics behind it, integral images essentially speed up the calculation of these Haar features. Instead of computing at every pixel, it instead creates sub-rectangles and creates array references for each of those sub-rectangles. These are then used to compute the Haar features.

3. Using Adaboost
Adaboost essentially chooses the best features and trains the classifiers to use them. It uses a combination of “weak classifiers” to create a “strong classifier” that the algorithm can use to detect objects.

4. Implementing Cascading Classifiers
The cascade classifier is made up of a series of stages, where each stage is a collection of weak learners. Weak learners are trained using boosting, which allows for a highly accurate classifier from the mean prediction of all weak learners.

Based on this prediction, the classifier either decides to indicate an object was found (positive) or move on to the next region (negative). Stages are designed to reject negative samples as fast as possible, because a majority of the windows do not contain anything of interest.

**LBPH ALGORITHM**

LBPH (Local Binary Pattern Histogram) is a Face-Recognition algorithm used to recognise a person's face. It is known for its performance and how it is able to recognize the face of a person from both front face and side face.

Local Binary Patterns Histogram algorithm was proposed in 2006. It is based on local binary operator. It is widely used in facial recognition due to its computational simplicity and discriminative power.

The steps involved to achieve this are:

Creating dataset\
Face acquisition\
Feature extraction\
Classification\
The LBPH algorithm is a part of opencv.

**DEMO OF THE PROJECT**

![](https://github.com/kritika-18/attendance-system/blob/main/project.gif)


The UI is created using tkinter library.

**DOCUMENTATIONS**

[Tkinter](https://docs.python.org/3/library/tkinter.html)
[OpenCV](https://pypi.org/project/opencv-python/)

