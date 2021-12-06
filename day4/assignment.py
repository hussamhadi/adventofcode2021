# coding=utf-8
"""
 Advent of code
"""
from datetime import datetime
from input import boards, numbers


def day4_1():
    board_length = len(boards[0])
    drawn_set = set(numbers[:4])
    for drawn_number in numbers[4:]:
        drawn_set.add(drawn_number)
        for board in boards:
            for i in range(0, board_length, 5):
                current_row_set = set(board[i:i+5])
                current_column_set = set(board[int(i/5)::5])
                if current_row_set.issubset(drawn_set):
                    return sum(set(board) - drawn_set) * drawn_number
                if current_column_set.issubset(drawn_set):
                    return sum(set(board) - drawn_set) * drawn_number


def day4_2():
    board_length = len(boards[0])
    drawn_set = set(numbers[:4])
    for drawn_number in numbers[4:]:
        drawn_set.add(drawn_number)
        for x, board in enumerate(boards):
            for i in range(0, board_length, 5):
                current_row_set = set(board[i:i+5])
                current_column_set = set(board[int(i/5)::5])
                if len(boards) > 1:
                    if current_row_set.issubset(drawn_set) or current_column_set.issubset(drawn_set):
                        boards.pop(x)
                else:
                    if current_row_set.issubset(drawn_set):
                        return sum(set(board) - drawn_set) * drawn_number
                    if current_column_set.issubset(drawn_set):
                        return sum(set(board) - drawn_set) * drawn_number


if __name__ == '__main__':
    durations = []
    no_of_runs = 1000
    print_result = False
    for i in range(no_of_runs):
        start = datetime.now()
        result = day4_2()
        if print_result:
            print("answer is {}".format(result))
        end = datetime.now()
        durations.append(end - start)

    durations = sum([x.microseconds for x in durations]) / no_of_runs
    print("took {} ms on average".format(durations/1000.0))
