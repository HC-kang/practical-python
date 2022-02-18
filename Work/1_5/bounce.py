def bounce(initHeight, numOfBounce, coef):
    height = initHeight
    for i in range(1, numOfBounce+1):
        height = round(height * coef, 4)
        print(i, height)


bounce(100, 10, 0.6)