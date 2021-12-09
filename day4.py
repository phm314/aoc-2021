def is_bingo(board: list[int]):
    for ind in range(5):
        row = board[ind*5:ind*5+5]
        col = board[ind::5]

        if all(row) or all(col):
            return True
        
    return False

def find_winning_board(boards: list[list[int]], numbers: list[int]):
    boolboards = [[0 for i in board] for board in boards]
    for number in numbers:
        for board_index, board in enumerate(boards):
            if number in board:
                boolboards[board_index][board.index(number)] = 1
                if is_bingo(boolboards[board_index]):
                    winner = boards[board_index]
                    return winner, boolboards[board_index], number
               
def find_last_winning_board(boards:list[list[int]], numbers: list[int]):
    boolboards = [[0 for i in board] for board in boards]
    playingboards: list[bool] = [1 for i in boards]
    for number in numbers:
        for board_index, board in enumerate(boards):
            if not playingboards[board_index]:
                continue
            if number in board:
                boolboards[board_index][board.index(number)] = 1
                if is_bingo(boolboards[board_index]):
                    playingboards[board_index] = 0
                    if not any(playingboards):
                        return boards[board_index], boolboards[board_index], number

def boardscore(board, bools, number):
    score = 0
    for index, b in enumerate(bools):
        if not b:
            score += board[index]
    return score * number

def part1():
    with open("inputs/day4.txt") as file:
        numbers   = []
        boards    = []
        boardrows = []
        
        for index, row in enumerate(file):
            if index == 0:
                numbers = [int(i.strip('\n,')) for i in row.split(',')]
            elif index > 1:
                if (row == '\n'):
                    boards.append(boardrows)
                    boardrows = []
                else:
                    boardrows.extend([int(i) for i in row.split()])
        boards.append(boardrows)

        winner = find_winning_board(boards, numbers)
        score = boardscore(*winner)
        print(score)
        
    # != 8148, unmarked squares
    # == 22680 

def part2():
    with open("inputs/day4.txt") as file:
        numbers   = []
        boards    = []
        boardrows = []
        
        for index, row in enumerate(file):
            if index == 0:
                numbers = [int(i.strip('\n,')) for i in row.split(',')]
            elif index > 1:
                if (row == '\n'):
                    boards.append(boardrows)
                    boardrows = []
                else:
                    boardrows.extend([int(i) for i in row.split()])
        boards.append(boardrows)
        last_winner = find_last_winning_board(boards, numbers)
        score = boardscore(*last_winner)
        print(score)

    # == 16168

