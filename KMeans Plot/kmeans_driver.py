"""
Connor Mentel
CS 5002 - Foundations
Programming #3
kmeans_driver.py
"""
import kmeans_viz
import random
from random import randint

COLORS = ['orange', 'brown', 'black', 'red']


def get_data():
    m = 1
    n = 100

    seen = []
    count = 0

    x, y = randint(m, n), randint(m, n)

    while count != 100:
        seen.append([x, y])
        x, y = randint(m, n), randint(m, n)
        while (x, y) in seen:
            x, y = randint(m, n), randint(m, n)

        count += 1
    return seen


# Function that calculates the Euclidean distance between points
def distance(point_one, point_two):
    return ((point_two[0] - point_one[0]) ** 2 + (point_two[1] - point_one[1]) ** 2) ** .5


# Function that is calculating the shortest distance between the data points in regards to centroids
def get_assignment(centroids, data):
    assignment = []

    # iterates through all of data
    for i in range(len(data)):

        # distances between each point and the centroids
        centroid_distances = []

        # to find closest centroid
        for j in centroids:
            # appends the distances to centroid_distance
            centroid_distances.append(distance(data[i], j))

        # smallest distance between a (undefined) centroid and data point
        minimum = min(centroid_distances)

        # finds position of 'minimum' in centroid_distances list
        indices = centroid_distances.index(minimum)

        # appending the list of the point from 'DATA' and the list of # 'centroids' to list 'assignment'
        assignment.append([i, indices])

    return assignment


# Main function that runs them functions and all from the viz file
def main():
    DATA = get_data()
    centroids = random.sample(DATA, 4)
    assignment = get_assignment(centroids, DATA)
    kmeans_viz.draw_centroids(centroids, COLORS)
    kmeans_viz.draw_assignment(centroids, DATA, assignment, COLORS)


main()
