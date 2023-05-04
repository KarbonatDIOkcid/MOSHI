import random
import numpy as math


def сalculateBestCombination(col):
    sum = 0
    for i in range(N):
        flag = 1
        for j in range(i):
            if math.absolute(i - j) == math.absolute(col[i] - col[j]):
                flag = 0
        sum += flag
    return sum


def chessBoard(positioning):
    for i in range(N):
        print("\n", "\b———————" * N, "\n|", end="")
        for j in range(N):
            if positioning[i] - 1 == j:
                print("  ⬤  |", end="")
            else:
                print("     |", end="")
    print("\n", "\b———————" * N)


N, iterationsConst = 19, 1000
positions = [i+1 for i in range(N)]
random.shuffle(positions)
bestPosition, temperature = сalculateBestCombination(positions), 1

for presentIterations in range(iterationsConst):
    if presentIterations < iterationsConst and bestPosition < N:
        temperature *= 0.99
        copiedPosition = positions.copy()
        firstRand, secondRand = random.randint(0, N - 1), random.randint(0, N - 1)
        copiedPosition[firstRand], copiedPosition[secondRand] = copiedPosition[secondRand], copiedPosition[firstRand]
        if сalculateBestCombination(copiedPosition) > bestPosition or random.uniform(0, 1) < math.exp((сalculateBestCombination(copiedPosition) - bestPosition) / temperature):
            positions = copiedPosition.copy()
            bestPosition = сalculateBestCombination(copiedPosition)

print("\nВідповідь у вигляді вектора: ", positions, "\n\nВідповідь у вигляді шахової дошки:", end="")
chessBoard(positions)
