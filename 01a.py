with open("input.txt") as file:
    curr = None
    prev = None
    increaseCount = 0
    nonIncreaseCount = 0
    totalCount = 0

    for line in file:
        totalCount += 1
        prev = curr
        curr = int(line.rstrip())

        if (prev != None and curr > prev):
            increaseCount += 1
        else:
            nonIncreaseCount += 1

    print("-----\nTotal increases: ", increaseCount, "\nTotal non-increases: ", nonIncreaseCount, "\nTotal inputs: ", totalCount)