# Implementation of the K-Means algorithm.
# Sebastian Oliver

def k_means(dataset):
    print("in k means")

def main():

    print("Hello")
    print("----------------------------------------------------------------")

    size = int(input("Enter the size of the dataset:\n"))
    print("----------------------------------------------------------------")

    print("Enter the coordinates of the data below in the form <x> <y>:")
    dataset = []
    for i in range(size):
        coords = input()
        coords.split(" ")
        dataset.append(coords)

    k_means(dataset)

if __name__ == "__main__":
    main()
