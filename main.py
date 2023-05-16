import random

def checkValid(grid):

    for r in range(0, 9):
        for c in range(0,9):
            if grid[r][c] == 0:
                return False
    return True


number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def fillGrid(grid):
    for i in range(0,81):
        row = i // 9
        col = i % 9

        if grid[row][col] == 0:
            random.shuffle(number_list)
            for value in number_list:
                if value not in grid[row]:
                    if value not in (grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col],
                                     grid[5][col], grid[6][col], grid[7][col], grid[8][col]):
                        square = []
                        if row < 3:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(0, 3)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(0, 3)]
                            else:
                                square = [grid[i][6:9] for i in range(0, 3)]
                        elif row < 6:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(3, 6)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(3, 6)]
                            else:
                                square = [grid[i][6:9] for i in range(3, 6)]
                        else:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(6, 9)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(6, 9)]
                            else:
                                square = [grid[i][6:9] for i in range(6, 9)]
                        if value not in (square[0] + square[1] + square[2]):
                            grid[row][col] = value
                            if checkValid(grid):
                                return True
                            else:
                                if fillGrid(grid):
                                    return True
            break
    grid[row][col] = 0

def printBoard(grid):

    for i in range(len(grid)):
        print(grid[i])

def main():


    #initialize board
    grid = [[0,0,0,0,0,0,0,0,0] for i in range(9)]

    #create complete board
    fillGrid(grid)
    printBoard(grid)
    print('\n')

    difficulty = 30
    attempts = 81
    while attempts > difficulty:
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        if grid[row][col] != 0:
            grid[row][col] = 0
            attempts -= 1
    printBoard(grid)
    print('\n')

    fillGrid(grid)

    printBoard(grid)

    print('\n')


if __name__ == '__main__':
    main()
