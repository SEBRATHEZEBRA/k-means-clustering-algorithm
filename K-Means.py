# Implementation of the K-Means algorithm.
# Sebastian Oliver (OLVSEB001)

import random
import math

dataset = []
centroids = []

# Initializing the dataset values to those in the brief.
dataset.append([2, 10, 0])
dataset.append([2, 5, 0])
dataset.append([8, 4, 0])
dataset.append([5, 8, 0])
dataset.append([7, 5, 0])
dataset.append([6, 4, 0])
dataset.append([1, 2, 0])
dataset.append([4, 9, 0])


# Calculates the euclidean distance between two points.
def distance(x1, y1, x2, y2):

    dist = math.sqrt((x1 -x2)**2 + (y1 - y2)**2)
    return dist


# Returns the index of the closest centroid to a point(x, y).
def getClosestCentroid(x, y):

    index = 1
    closest = distance(x, y, centroids[0][0], centroids[0][1])

    for i in range(1, len(centroids)):
        dist = distance(x, y, centroids[i][0], centroids[i][1])
        if dist < closest:
            closest = dist
            index = i + 1

    return index

# Sets the new centroids from the mean of the points in the current centroid.
def setCentroids():

    avg1x = 0
    avg1y = 0
    count1 = 0

    avg2x = 0
    avg2y = 0
    count2 = 0

    avg3x = 0
    avg3y = 0
    count3 = 0

    for i in range(len(dataset)):
        if dataset[i][2] == 1:

            avg1x += dataset[i][0]
            avg1y += dataset[i][1]
            count1 += 1

        elif dataset[i][2] == 2:

            avg2x += dataset[i][0]
            avg2y += dataset[i][1]
            count2 += 1

        elif dataset[i][2] == 3:

            avg3x += dataset[i][0]
            avg3y += dataset[i][1]
            count3 += 1

    avg1x = avg1x / count1
    avg1y = avg1y / count1

    avg2x = avg2x / count2
    avg2y = avg2y / count2

    avg3x = avg3x / count3
    avg3y = avg3y / count3

    centroids[0][0] = avg1x
    centroids[0][1] = avg1y

    centroids[1][0] = avg2x
    centroids[1][1] = avg2y

    centroids[2][0] = avg3x
    centroids[2][1] = avg3y


# Performs the K-Means algorithm on the dataset.
def k_means():

    clusters = 3

    # Initializing data into random clusters.
    for i in range(len(dataset)):
        dataset[i][2] = random.randint(1, clusters)
        print(dataset[i])

    # Setting the original centroids.
    centroids.append(dataset[0])
    centroids.append(dataset[3])
    centroids.append(dataset[6])

    # Changing the assigned clusters of the original centroids.
    dataset[0][2] = 1
    dataset[3][2] = 2
    dataset[6][2] = 3

    # Calculating the closet centroid for each point in the dataset.
    closest = -1
    for i in range(len(dataset)):
        closest = getClosestCentroid(dataset[i][0], dataset[i][1])
        dataset[i][2] = closest

    setCentroids()

    for i in range(len(centroids)):
        print(centroids[i])


# The main method for the program.
def main():

    print("Hello")
    print("----------------------------------------------------------------")

    k_means()


if __name__ == "__main__":
    main()
