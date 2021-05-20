# Implementation of the K-Means algorithm.
# Sebastian Oliver

import random
import math

dataset = []
centroids = []

def distance(x1, y1, x2, y2):

    dist = math.sqrt((x1 -x2) ^ 2 + (y1 - y2) ^ 2)
    return dist

# Returns the index of the closest centroid to a point(x, y)
def getClosestCentroid(x, y):

    index = centroids[0]
    closest = distance(x, y, dataset[centroid[0]][0], dataset[centroid[0]][1])

    for i in range(1, len(centroids)):
        dist = distance(x, y, dataset[centroid[i]][0], dataset[centroid[i]][1])
        if dist < closest:
            closest = dist
            index = centroids[i]

    return index

def k_means():

    clusters = 3

    # Initializing data into random clusters.
    for i in range(len(dataset)):
        dataset[i].append(random.randint(1, clusters))
        print(dataset[i])

    centroids.append(0)
    centroids.append(3)
    centroids.append(6)


    for i in range(clusters):
        dataset[centroids[i]][2] = i + 1

    closest = -1
    for i in range(len(dataset)):
        closest = getClosestCentroid(dataset[i][0], dataset[i][1])
        dataset[i][2] = closest


def main():

    print("Hello")
    print("----------------------------------------------------------------")

    size = int(input("Enter the size of the dataset:\n"))
    print("----------------------------------------------------------------")

    print("Enter the coordinates of the data below in the form <x> <y>:")
    for i in range(size):
        coords = input()
        coords = coords.split()
        coords[0] = int(coords[0])
        coords[1] = int(coords[1])

        dataset.append(coords)

    #k_means()

    #print(distance(1, 4, 3, 7))


if __name__ == "__main__":
    main()
