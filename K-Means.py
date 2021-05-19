# Implementation of the K-Means algorithm.
# Sebastian Oliver

import random

def k_means(dataset):

    clusters = 3

    # Initializing data into random clusters.
    for i in range(len(dataset)):
        dataset[i].append(random.randint(1, clusters))
        print(dataset[i])

    centroids = []


def main():

    print("Hello")
    print("----------------------------------------------------------------")

    size = int(input("Enter the size of the dataset:\n"))
    print("----------------------------------------------------------------")

    print("Enter the coordinates of the data below in the form <x> <y>:")
    dataset = []
    for i in range(size):
        coords = input()
        coords = coords.split()
        coords[0] = int(coords[0])
        coords[1] = int(coords[1])
        
        dataset.append(coords)

    k_means(dataset)

if __name__ == "__main__":
    main()
