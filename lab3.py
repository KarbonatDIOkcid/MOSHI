import random
import matplotlib.pyplot as plot
import numpy as math


def pointCreate(points):
    return points.append([random.uniform(0, 1), random.uniform(0, 1)])


def pointSpaceFill(amount):
    points = []
    while amount > len(points):
        pointCreate(points)
    return points


def measureCalculating(firstX, firstY, secondX, secondY):
    return math.sqrt((secondX - firstX) **2 + (secondY - firstY) ** 2)


def comparisonClusters(measures):
    min, i, index = measures[0], 1, 0
    for i in range(len(measures)):
        if measures[i] < min:
            min = measures[i]
            index = i
    return index


def clustering(points, centers, amount, clusterAmount):
    clusters, num = [[] for i in range(clusterAmount)], 0
    while num < amount:
        measures = []
        for i in range(clusterAmount):
            measures.append(measureCalculating(points[num][0], points[num][1], centers[i][0], centers[i][1]))
        clusters[comparisonClusters(measures)].append(points[num])
        num += 1
    return clusters


def newCenterFindingMeans(cluster):
    sumX, sumY = 0, 0
    for i in range(len(cluster)):
        sumX += cluster[i][0]
        sumY += cluster[i][1]
    return [sumX / len(cluster), sumY / len(cluster)]


def mainFunction(amount, clusterAmount, points, centers):
    cluster = []
    while True:
        for i in range(clusterAmount):
            if len(centers) < clusterAmount*2 or centers[-i] != centers[-i - K]:
                cluster = clustering(points, centers, amount, clusterAmount)
                for j in range(clusterAmount):
                    centers.append(newCenterFindingMeans(cluster[j]))
            else:
                return cluster


def createGraph(clusters):
    graph, ax = plot.subplots(1, 1, figsize=(10, 10))
    ax.set_title("Кількість кластерів " + str(K), fontsize=18)
    plot.grid(True)
    for i in range(len(clusters)):
        color = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        for j in range(len(clusters[i])):
            ax.scatter(clusterCenters[i-K][0], clusterCenters[i-K][1], color=color, marker='o', s=200)
            ax.scatter(clusters[i][j][0], clusters[i][j][1], color=color, s=20)
    plot.xlim(0, 1.4)
    plot.ylim(0, 1.4)
    plot.show()


N, K = 1750, 33

pointSpace = pointSpaceFill(N)
clusterCenters = [pointSpace[random.randint(0, N - 1)] for i in range(K)]
clusters = mainFunction(N, K, pointSpace, clusterCenters)

createGraph(clusters)