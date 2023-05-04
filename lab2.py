import numpy as math
from scipy import integrate
import random
import matplotlib.pyplot as plot


def elementaryFunction(x):
    return -x ** 2 + math.sin(10 * x) + 2


def complexFunction(x):
    return math.exp(x ** 2)


def functionIntegrate(function, start, end):
    square = integrate.quad(function, start, end)
    return square[0]


def valueCalculate(value, flag):
    return elementaryFunction(value) if flag == 0 else complexFunction(value)


def pointCreate(startX, endX, startY, endY):
    return [random.uniform(startX, endX), random.uniform(startY, endY)]


def YLimitsFinding(startX, endX, identifier, step):
    maxY, minY = valueCalculate(startX, identifier), valueCalculate(startX, identifier)
    presentX, presentY = startX, valueCalculate(startX, identifier)
    while presentX < endX:
        presentY = valueCalculate(presentX, identifier)
        maxY = max(maxY, presentY)
        minY = min(minY, presentY)
        presentX += step
    return [math.floor(minY), math.round(maxY)]


def squarePointsCalculate(points, identifier):
    amount = 0
    for i in range(len(points)):
        if valueCalculate(points[i][0], identifier) > points[i][1]:
            amount += 1
    return amount


def graphCreate(points, startX, endX, startY, endY, identifier):
    graph, ax = plot.subplots(1, 1, figsize=(8, 8))
    plot.grid(True)
    x = math.linspace(startX, endX)
    plot.plot(x, valueCalculate(x, identifier), linewidth=3, color="black", label='Function')
    for i in range(len(points)):
        if valueCalculate(points[i][0], identifier) > points[i][1]:
            ax.scatter(points[i][0], points[i][1], color='green', s=15)
        else:
            ax.scatter(points[i][0], points[i][1], color='blue', s=15)
    plot.xlim(startX - identifier, endX + identifier)
    plot.ylim(startY - identifier, endY + identifier)
    plot.legend()
    plot.show()


def messagePrint(trueSquare, square, absoluteError):
    print("Точне значення площі:", "\t"*4, trueSquare)
    print("Значення площі методом Монте-Карло: ", square)
    print("Абсолютна похибка:", "\t"*5, math.round(absoluteError, 5))
    print("Відносна похибка:", "\t"*5, math.round(absoluteError / trueSquare * 100, 5), "\b%")


elementaryX, complexX = [0, 1], [1, 2]
iterations, pointSpaceComplex, pointSpaceElementary = 15, [], []
elementaryY, complexY = YLimitsFinding(elementaryX[0], elementaryX[1], 0, 0.1), YLimitsFinding(complexX[0], complexX[1], 1, 0.001)

for i in range(iterations):
    pointSpaceComplex.append(pointCreate(complexX[0], complexX[1], complexY[0], complexY[1]))
    pointSpaceElementary.append(pointCreate(elementaryX[0], elementaryX[1], elementaryY[0], elementaryY[1]))

graphCreate(pointSpaceComplex, complexX[0], complexX[1], complexY[0], complexY[1], 1)
graphCreate(pointSpaceElementary, elementaryX[0], elementaryX[1], elementaryY[0], elementaryY[1], 0)

squarePointsElementary, squarePointsComplex = squarePointsCalculate(pointSpaceElementary, 0), squarePointsCalculate(pointSpaceComplex, 1)

squareElementary = (elementaryY[1] - elementaryY[0]) * (elementaryX[1] - elementaryX[0]) * (squarePointsElementary / iterations)
squareComplex = (complexY[1] - complexY[0]) * (complexX[1] - complexX[0]) * (squarePointsComplex / iterations)
trueSquareElementary, trueSquareComplex = functionIntegrate(elementaryFunction, elementaryX[0], elementaryX[1]), functionIntegrate(complexFunction, complexX[0], complexX[1])
absoluteErrorElementary, absoluteErrorComplex = math.absolute(trueSquareElementary - squareElementary), math.absolute(trueSquareComplex - squareComplex)

print("\nОбчислені дані для тестової функції:\n")
messagePrint(trueSquareElementary, squareElementary, absoluteErrorElementary)
print("\n\nОбчислені дані для основної функції:\n")
messagePrint(trueSquareComplex, squareComplex, absoluteErrorComplex)
