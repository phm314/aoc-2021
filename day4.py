def part1():
    with open("inputs/day4.txt") as file:
        numbers   = []
        boards    = []
        boardrows = []
        
        for index, row in enumerate(file):
            if index == 0:
                numbers = [int(i.strip('\n,')) for i in row.split(',')]
            elif index == 1:
                pass
            else:
                if (row == '\n'):
                    boards.append(boardrows)
                    boardrows = []
                else:
                    boardrows.extend([int(i) for i in row.split()])

        boards.append(boardrows)
        print(numbers)
        for board in boards:
            print(board)
        print(len(boards))

        boolboards = [[0 for i in board] for board in boards]

        for number in numbers:
            for board_index, board in enumerate(boards):
                if number in board:
                    print(board_index, end=", ")
                    print(board.index(number))
                    boolboards[board_index][board.index(number)] = 1
            
                    if is_bingo(boolboards[board_index]):
                        print(board_index)
                        break
        

import os
os.system("cls")
part1()
