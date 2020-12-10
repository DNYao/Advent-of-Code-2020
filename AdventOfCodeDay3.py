######################################
# Advent of Code 2020 Challenge
# Day 3
######################################

#Combined Part 1 and Part 2 solution inputs. Part 1 input is (3,1)
myList = [(1,1), (3,1), (5,1), (7,1), (1,2)]

def tobogganPath(hillMap, xValue, yValue):
    '''
    Tree-checking function of the Day 3 puzzle.
    :param hillMap: The content of the Day3HillsAndTrees.txt file.
    :param xValue: Your lateral movement.
    :param yValue: Your vertical movement.
    '''
    hillLines = []
    trees = 0
    xPosition = 0
    yPosition = 0

    for line in hillMap:
        hillLines.append(line[:len(line)-1])

    while xPosition != len(hillLines):
# If we get an index error in this case, 
# it's due to reaching the end of the "hill", 
# so we may as well just return the current tree value
        try:
            if hillLines[xPosition][yPosition] == '#':
                trees += 1

            xPosition += xValue
            yPosition += yValue
            yPosition %= len(hillLines[0])

        except IndexError:
            return(trees)

    return(trees)

def completeSolutions(myList):
    '''
    Calls tobagganPath() and uses output to create solutions.
    :param myList: list of the x and y values for your toboggan.
    '''
    partTwoValues = []
    partTwoSolution = 1

    for i in myList:
        with open('Day3HillsAndTrees.txt', 'r') as hillMap:
            yValue = i[0]
            xValue = i[1]
            outPut = tobogganPath(hillMap, xValue, yValue)

        partTwoValues.append(outPut)

    for i in partTwoValues:
        partTwoSolution *= i

    print('Part 1: ', partTwoValues[1])
    print('Part 2: ', partTwoSolution)

completeSolutions(myList)
